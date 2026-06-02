from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select

from app.keyboards.inline import lesson_menu_kb
from app.models.user import User
from app.services.lesson_context import get_lesson_context, lesson_header
from app.services.lesson_service import get_lesson_by_id
from app.services.llm_prompts import DEBUG_CODE_RULES, TELEGRAM_MARKDOWN_RULES
from app.services.llm_service import LLMNotConfiguredError, LLMRequestError, chat
from app.services.user_profile_prompt import build_user_profile_prompt
from app.services.telegram_format import answer_html
from app.services.progress_service import get_last_test_percent
from config import get_settings
from database import SessionLocal

router = Router()
settings = get_settings()


class AskState(StatesGroup):
    waiting_question = State()


class DebugState(StatesGroup):
    waiting_code = State()


async def _resolve_lesson_id(state: FSMContext, telegram_id: int) -> int | None:
    data = await state.get_data()
    if data.get("context_lesson_id"):
        return int(data["context_lesson_id"])
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == telegram_id))
        if user and user.current_lesson_id:
            return user.current_lesson_id
    return None


async def _send_llm_reply(message: Message, text: str, lesson_id: int, *, show_extra: bool = False) -> None:
    await answer_html(message, text)
    await message.answer("✅ Готово.", reply_markup=lesson_menu_kb(lesson_id, show_extra_tasks=show_extra))


async def _run_llm(
    message: Message,
    system: str,
    user: str,
    lesson_id: int,
    show_extra: bool = False,
    telegram_id: int | None = None,
) -> None:
    wait = await message.answer("⏳ Думаю...")

    profile_prompt = ""

    if telegram_id is not None:
        with SessionLocal() as db:
            db_user = db.scalar(select(User).where(User.telegram_id == telegram_id))
            profile_prompt = build_user_profile_prompt(db_user)

    if profile_prompt:
        system = f"{system}\n\n{profile_prompt}"

    try:
        answer = await chat(system=system, user=user)
    except LLMNotConfiguredError as e:
        await wait.edit_text(str(e))
        return
    except LLMRequestError as e:
        await wait.edit_text(f"Ошибка LLM: {e}")
        return

    await wait.delete()
    await _send_llm_reply(message, answer, lesson_id, show_extra=show_extra)


@router.callback_query(lambda c: c.data and c.data.startswith("llm:explain:"))
async def explain_simpler(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":")[2])
    await state.update_data(context_lesson_id=lesson_id)
    with SessionLocal() as db:
        try:
            lesson, text = get_lesson_context(db, lesson_id)
        except (ValueError, FileNotFoundError) as e:
            await callback.message.answer(str(e))
            await callback.answer()
            return
    system = (
        "Ты преподаватель Python для начинающих. Объясняй простым русским языком, "
        "коротко, с одним понятным примером кода. Не выходи за тему урока.\n\n"
        + TELEGRAM_MARKDOWN_RULES
    )
    user = f"Урок:\n{text}\n\nОбъясни материал урока проще, как для новичка. Добавь мини-пример кода."
    await _run_llm(callback.message, system, user, lesson_id, telegram_id=callback.from_user.id)
    await callback.answer()


@router.message(Command("ask"))
async def cmd_ask(message: Message, state: FSMContext) -> None:
    lesson_id = await _resolve_lesson_id(state, message.from_user.id)
    if not lesson_id:
        await message.answer("Сначала выберите урок в /lessons, затем снова /ask")
        return
    await state.update_data(context_lesson_id=lesson_id, ask_lesson_id=lesson_id)
    await state.set_state(AskState.waiting_question)
    with SessionLocal() as db:
        lesson = get_lesson_by_id(db, lesson_id)
    await message.answer(
        f"💬 Задайте вопрос по теме: <b>{lesson.lesson_number}</b> — {lesson.title}\n\n"
        "Напишите один сообщением.",
        parse_mode="HTML",
    )


@router.message(AskState.waiting_question)
async def process_ask(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lesson_id = data.get("ask_lesson_id") or data.get("context_lesson_id")
    if not lesson_id:
        await message.answer("Контекст урока потерян. Откройте /lessons")
        await state.clear()
        return
    question = (message.text or "").strip()
    if not question:
        await message.answer("Напишите вопрос текстом")
        return
    with SessionLocal() as db:
        try:
            lesson, text = get_lesson_context(db, int(lesson_id))
        except (ValueError, FileNotFoundError) as e:
            await message.answer(str(e))
            await state.clear()
            return
    system = (
        "Ты помощник по курсу Python. Отвечай только по теме текущего урока. "
        "Если вопрос не по теме — вежливо скажи об этом. Отвечай по-русски, кратко и понятно.\n\n"
        + TELEGRAM_MARKDOWN_RULES
    )
    user = f"Контекст урока ({lesson_header(lesson)}):\n{text}\n\nВопрос студента:\n{question}"
    await state.clear()
    await _run_llm(message, system, user, int(lesson_id), telegram_id=message.from_user.id)


async def _prompt_debug_code(message: Message, state: FSMContext, lesson_id: int) -> None:
    await state.update_data(context_lesson_id=lesson_id, debug_lesson_id=lesson_id)
    await state.set_state(DebugState.waiting_code)
    with SessionLocal() as db:
        lesson = get_lesson_by_id(db, lesson_id)
    await message.answer(
        f"🐞 <b>Разбор кода</b> — урок {lesson.lesson_number}\n\n"
        "Отправьте код одним сообщением (можно с текстом ошибки).",
        parse_mode="HTML",
    )


@router.message(Command("debug"))
async def cmd_debug(message: Message, state: FSMContext) -> None:
    lesson_id = await _resolve_lesson_id(state, message.from_user.id)
    if not lesson_id:
        await message.answer("Сначала выберите урок в /lessons")
        return
    await _prompt_debug_code(message, state, lesson_id)


@router.callback_query(lambda c: c.data and c.data.startswith("llm:debug:"))
async def cb_debug(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":")[2])
    await _prompt_debug_code(callback.message, state, lesson_id)
    await callback.answer()


@router.message(DebugState.waiting_code)
async def process_debug(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lesson_id = int(data.get("debug_lesson_id") or data.get("context_lesson_id") or 0)
    code = (message.text or "").strip()
    if not code or not lesson_id:
        await message.answer("Пришлите код текстом")
        return
    with SessionLocal() as db:
        try:
            lesson, text = get_lesson_context(db, lesson_id)
        except (ValueError, FileNotFoundError) as e:
            await message.answer(str(e))
            await state.clear()
            return
    system = (
        "Ты преподаватель Python. Разбери только присланный код студента: ошибки, причина, исправление. "
        "Отвечай по-русски. Если код верный — кратко похвали.\n\n"
        + DEBUG_CODE_RULES
        + "\n\n"
        + TELEGRAM_MARKDOWN_RULES
    )
    user = (
        f"Тема урока ({lesson_header(lesson)}), краткий контекст:\n{text[:2000]}\n\n"
        f"Код студента:\n```python\n{code}\n```"
    )
    await state.clear()
    await answer_html(message, f"**Ваш код:**\n\n```python\n{code}\n```")
    await _run_llm(message, system, user, lesson_id, telegram_id=message.from_user.id)


@router.callback_query(lambda c: c.data and c.data.startswith("llm:extra:"))
async def extra_tasks(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":")[2])
    await state.update_data(context_lesson_id=lesson_id)
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        try:
            lesson, text = get_lesson_context(db, lesson_id)
        except (ValueError, FileNotFoundError) as e:
            await callback.message.answer(str(e))
            await callback.answer()
            return
        pct = get_last_test_percent(db, user.id, lesson_id) if user else None
    system = (
        "Ты автор задач по Python. Сгенерируй 3–5 дополнительных учебных задач по теме урока "
        "для закрепления. Формат: нумерованный список, для каждой — формулировка и краткая подсказка. "
        "Без решений. Уровень — начинающий.\n\n"
        + TELEGRAM_MARKDOWN_RULES
    )
    extra = f"\nПоследний результат мини-теста: {pct}%." if pct is not None else ""
    user = f"Урок:\n{text}{extra}\n\nСгенерируй дополнительные задачи."
    await _run_llm(
    callback.message,
    system,
    user,
    lesson_id,
    show_extra=True,
    telegram_id=callback.from_user.id,
)
    await callback.answer()
