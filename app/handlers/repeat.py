from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from app.models.lesson import Lesson
from app.models.user import User
from app.services.progress_service import today_repetitions
from database import SessionLocal

router = Router()


@router.message(Command("repeat"))
async def cmd_repeat(message: Message) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == message.from_user.id))
        if not user:
            await message.answer("Сначала /start")
            return
        reps = today_repetitions(db, user.id)
        if not reps:
            await message.answer("Сегодня повторений нет")
            return
        lines = ["Сегодня повторяем:"]
        for rep in reps:
            lesson = db.get(Lesson, rep.lesson_id)
            if lesson:
                lines.append(f"- {lesson.lesson_number} {lesson.title} (через {rep.interval_days} дн.)")
        await message.answer("\n".join(lines))
