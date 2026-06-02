from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy import select

from app.keyboards.inline import lesson_menu_kb, test_options_kb
from app.models.lesson import Lesson
from app.models.user import User
from app.services.progress_service import save_test_result
from app.services.telegram_format import answer_html
from app.services.test_service import load_test_file
from app.services.mistake_service import add_user_mistake
from config import get_settings
from database import SessionLocal

router = Router()
settings = get_settings()


@router.callback_query(lambda c: c.data and c.data.startswith("test:"))
async def start_test(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":", 1)[1])
    await state.update_data(context_lesson_id=lesson_id)
    with SessionLocal() as db:
        lesson = db.get(Lesson, lesson_id)
    if not lesson:
        await callback.message.answer("Урок не найден")
        await callback.answer()
        return
    try:
        questions = load_test_file(settings.tests_dir, lesson.lesson_number)
    except FileNotFoundError as e:
        await callback.message.answer(str(e))
        await callback.answer()
        return
    await state.update_data(test_lesson_id=lesson_id, test_questions=questions, test_score=0)
    q = questions[0]
    await callback.message.answer(f"Вопрос 1/{len(questions)}\n{q['question']}", reply_markup=test_options_kb(lesson_id, 0, q["options"]))
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("tans:"))
async def answer_test(callback: CallbackQuery, state: FSMContext) -> None:
    _, lesson_s, q_idx_s, option_s = callback.data.split(":")
    lesson_id, q_idx, opt_idx = int(lesson_s), int(q_idx_s), int(option_s)
    data = await state.get_data()
    questions = data.get("test_questions", [])
    score = data.get("test_score", 0)
    if not questions or q_idx >= len(questions):
        await callback.message.answer("Тест не активен")
        await callback.answer()
        return
    q = questions[q_idx]
    ok = q["correct_index"] == opt_idx

    if ok:
        score += 1
    else:
        with SessionLocal() as db:
            user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
            if user:
                selected_answer = q["options"][opt_idx]
                correct_answer = q["options"][q["correct_index"]]

                add_user_mistake(
                    db,
                    user_id=user.id,
                    lesson_id=lesson_id,
                    source="test",
                    topic=q["question"][:128],
                    description=(
                        f"Вопрос: {q['question']}\n"
                        f"Ответ пользователя: {selected_answer}\n"
                        f"Правильный ответ: {correct_answer}\n"
                        f"Объяснение: {q.get('explanation', '-')}"
                    ),
                )
    verdict = "✅ **Верно**" if ok else "❌ **Неверно**"
    await answer_html(callback.message, f"{verdict}\n\n{q.get('explanation', '-')}")
    nxt = q_idx + 1
    if nxt < len(questions):
        nq = questions[nxt]
        await state.update_data(test_score=score)
        await callback.message.answer(f"Вопрос {nxt + 1}/{len(questions)}\n{nq['question']}", reply_markup=test_options_kb(lesson_id, nxt, nq["options"]))
    else:
        with SessionLocal() as db:
            user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
            if user:
                save_test_result(db, user.id, lesson_id, score, len(questions))
        pct = round((score / len(questions)) * 100, 2)
        advise = "Рекомендуется повторить тему" if pct < 60 else "Отлично, можно идти дальше"
        await callback.message.answer(
            f"Тест завершён: {score}/{len(questions)} ({pct}%). {advise}",
            reply_markup=lesson_menu_kb(lesson_id, show_extra_tasks=pct < 60),
        )
        await state.clear()
    await callback.answer()
