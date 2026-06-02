from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select

from app.keyboards.inline import lessons_list_kb
from app.models.lesson import Lesson
from app.models.user import User
from app.services.lesson_service import get_lessons_with_status
from app.services.progress_service import build_user_progress_summary
from database import SessionLocal

router = Router()


async def _send_progress(message: Message, telegram_id: int) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            await message.answer("Сначала /start")
            return
        cur = db.get(Lesson, user.current_lesson_id) if user.current_lesson_id else None
        s = build_user_progress_summary(db, user.id)
        tests = "\n".join([f"- Урок {t.lesson_id}: {t.score}/{t.total_questions}" for t in s["tests"]]) or "Пока нет"
        items = get_lessons_with_status(db, user.id)
        await message.answer(
            f"Текущий модуль: {cur.module_number if cur else '-'}\n"
            f"Текущий урок: {cur.lesson_number if cur else '-'} {cur.title if cur else ''}\n"
            f"Завершено уроков: {s['completed_lessons']}\n"
            f"Решено задач: {s['solved_tasks']}/{s['total_tasks']}\n"
            f"Общий процент: {s['overall_percent']}%\n"
            f"Последние тесты:\n{tests}",
            reply_markup=lessons_list_kb(items),
        )


@router.message(Command("progress"))
async def cmd_progress(message: Message) -> None:
    await _send_progress(message, message.from_user.id)


@router.callback_query(lambda c: c.data == "show_progress")
async def cb_progress(callback: CallbackQuery) -> None:
    await _send_progress(callback.message, callback.from_user.id)
    await callback.answer()
