from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select

from app.keyboards.inline import lesson_menu_kb, task_choice_kb, task_practice_kb
from app.models.user import User
from app.services.lesson_service import get_lesson_by_id
from app.services.progress_service import update_tasks_progress
from app.services.task_service import check_task_answer, load_tasks_file
from app.services.mistake_service import add_user_mistake
from config import get_settings
from database import SessionLocal

router = Router()
settings = get_settings()


class PracticeState(StatesGroup):
    waiting_answer = State()


@router.callback_query(lambda c: c.data and c.data.startswith("practice:"))
async def start_practice(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":", 1)[1])
    with SessionLocal() as db:
        lesson = get_lesson_by_id(db, lesson_id)
    if not lesson:
        await callback.answer("Урок не найден", show_alert=True)
        return
    try:
        tasks = load_tasks_file(settings.tasks_dir, lesson.lesson_number)
    except FileNotFoundError as e:
        await callback.message.answer(str(e), reply_markup=lesson_menu_kb(lesson_id))
        await callback.answer()
        return
    await state.update_data(
        practice_lesson_id=lesson_id,
        practice_tasks=tasks,
        practice_idx=0,
        practice_solved=0,
        context_lesson_id=lesson_id,
    )
    await _send_task(callback.message, state, lesson_id, tasks, 0)
    await callback.answer()


async def _send_task(message: Message, state: FSMContext, lesson_id: int, tasks: list[dict], idx: int) -> None:
    total = len(tasks)
    task = tasks[idx]
    title = task.get("title") or f"Задача {idx + 1}"
    body = task.get("question", task.get("description", ""))
    text = f"<b>✏️ {title}</b> ({idx + 1}/{total})\n\n{body}"
    if task.get("type") == "choice":
        await state.set_state(None)
        await message.answer(text, reply_markup=task_choice_kb(lesson_id, idx, task["options"]), parse_mode="HTML")
    else:
        await state.set_state(PracticeState.waiting_answer)
        await message.answer(
            text + "\n\n<i>Отправьте ответ сообщением.</i>",
            reply_markup=task_practice_kb(lesson_id, idx),
            parse_mode="HTML",
        )


@router.callback_query(lambda c: c.data and c.data.startswith("tchk:"))
async def answer_choice_task(callback: CallbackQuery, state: FSMContext) -> None:
    _, lesson_s, idx_s, opt_s = callback.data.split(":")
    lesson_id, idx, opt_idx = int(lesson_s), int(idx_s), int(opt_s)
    data = await state.get_data()
    tasks = data.get("practice_tasks", [])
    if not tasks or idx >= len(tasks):
        await callback.answer("Практика не активна", show_alert=True)
        return
    task = tasks[idx]
    ok = task.get("correct_index") == opt_idx
    feedback = task.get("explanation", "Верно!" if ok else "Неверно.")
    if not ok:
        selected_answer = task["options"][opt_idx]
        correct_answer = task["options"][task["correct_index"]]

        _save_task_mistake(
            callback.from_user.id,
            lesson_id,
            task,
            "task_choice",
            (
                f"Неверный ответ в задаче.\n"
                f"Вопрос: {task.get('question', '-')}\n"
                f"Ответ пользователя: {selected_answer}\n"
                f"Правильный ответ: {correct_answer}\n"
                f"Объяснение: {task.get('explanation', '-')}"
            ),
        )
    await callback.message.answer(("✅ " if ok else "❌ ") + feedback)
    solved = data.get("practice_solved", 0) + (1 if ok else 0)
    await _advance(callback.message, state, callback.from_user.id, lesson_id, tasks, idx, solved)
    await callback.answer()


@router.message(PracticeState.waiting_answer)
async def answer_text_task(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    tasks = data.get("practice_tasks", [])
    idx = data.get("practice_idx", 0)
    lesson_id = data.get("practice_lesson_id")
    if not tasks or lesson_id is None:
        await message.answer("Практика не активна.")
        await state.clear()
        return
    task = tasks[idx]
    answer = message.text or ""
    ok, feedback = await check_task_answer(task, answer)

    if not ok:
        _save_task_mistake(
            message.from_user.id,
            lesson_id,
            task,
            "task_answer",
            (
                f"Неверный ответ в практической задаче.\n"
                f"Задание: {task.get('question', '-')}\n"
                f"Ответ пользователя: {answer[:500]}\n"
                f"Ожидаемое решение: {task.get('solution', '-')}\n"
                f"Объяснение: {task.get('explanation', '-')}"
            ),
        )

    await message.answer(("✅ " if ok else "❌ ") + feedback)
    solved = data.get("practice_solved", 0) + (1 if ok else 0)
    await _advance(message, state, message.from_user.id, lesson_id, tasks, idx, solved)


@router.callback_query(lambda c: c.data and c.data.startswith("thint:"))
async def task_hint(callback: CallbackQuery, state: FSMContext) -> None:
    idx = int(callback.data.split(":")[2])
    data = await state.get_data()
    tasks = data.get("practice_tasks", [])
    if idx < len(tasks):
        hint = tasks[idx].get("hint", "Подсказка не задана")
        await callback.message.answer(f"💡 <b>Подсказка:</b>\n{hint}", parse_mode="HTML")
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("tsol:"))
async def task_solution(callback: CallbackQuery, state: FSMContext) -> None:
    _, lesson_s, idx_s = callback.data.split(":")
    lesson_id, idx = int(lesson_s), int(idx_s)

    data = await state.get_data()
    tasks = data.get("practice_tasks", [])

    if idx < len(tasks):
        task = tasks[idx]
        sol = task.get("solution", "Решение не задано")

        _save_task_mistake(
            callback.from_user.id,
            lesson_id,
            task,
            "task_solution",
            (
                f"Пользователь запросил готовое решение.\n"
                f"Задание: {task.get('question', '-')}\n"
                f"Решение: {sol}\n"
                f"Объяснение: {task.get('explanation', '-')}"
            ),
        )

        await callback.message.answer(
            f"📋 <b>Ответ:</b>\n<pre><code>{sol}</code></pre>",
            parse_mode="HTML",
        )

    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("tskip:"))
async def skip_task(callback: CallbackQuery, state: FSMContext) -> None:
    _, lesson_s, idx_s = callback.data.split(":")
    lesson_id, idx = int(lesson_s), int(idx_s)
    data = await state.get_data()
    tasks = data.get("practice_tasks", [])
    solved = data.get("practice_solved", 0)
    if idx < len(tasks):
        task = tasks[idx]
        _save_task_mistake(
            callback.from_user.id,
            lesson_id,
            task,
            "task_skip",
            (
                f"Пользователь пропустил задачу.\n"
                f"Задание: {task.get('question', '-')}\n"
                f"Подсказка: {task.get('hint', '-')}\n"
                f"Объяснение: {task.get('explanation', '-')}"
            ),
        )
    await _advance(callback.message, state, callback.from_user.id, lesson_id, tasks, idx, solved)
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("tsolved:"))
async def mark_task_solved(callback: CallbackQuery, state: FSMContext) -> None:
    _, lesson_s, idx_s = callback.data.split(":")
    lesson_id, idx = int(lesson_s), int(idx_s)
    data = await state.get_data()
    tasks = data.get("practice_tasks", [])
    solved = data.get("practice_solved", 0) + 1
    await callback.message.answer("✅ Засчитано!")
    await _advance(callback.message, state, callback.from_user.id, lesson_id, tasks, idx, solved)
    await callback.answer()


async def _advance(
    message: Message,
    state: FSMContext,
    telegram_id: int,
    lesson_id: int,
    tasks: list[dict],
    idx: int,
    solved: int,
) -> None:
    nxt = idx + 1
    total = len(tasks)
    if nxt < total:
        await state.update_data(practice_idx=nxt, practice_solved=solved)
        await _send_task(message, state, lesson_id, tasks, nxt)
        return
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == telegram_id))
        if user:
            update_tasks_progress(db, user.id, lesson_id, min(solved, total), total)
    await state.clear()
    await message.answer(
        f"🎯 Практика завершена: {min(solved, total)}/{total}.",
        reply_markup=lesson_menu_kb(lesson_id),
    )

def _save_task_mistake(
    telegram_id: int,
    lesson_id: int,
    task: dict,
    source: str,
    description: str,
) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            return

        add_user_mistake(
            db,
            user_id=user.id,
            lesson_id=lesson_id,
            source=source,
            topic=task.get("title", "Практическая задача")[:128],
            description=description,
        )