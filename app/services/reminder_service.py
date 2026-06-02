from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot
from sqlalchemy import select

from app.models.lesson import Lesson
from app.models.user import User
from database import SessionLocal

scheduler = AsyncIOScheduler()


async def send_daily_reminder(bot: Bot, user_id: int, lesson_title: str, lesson_number: str) -> None:
    await bot.send_message(user_id, f"Привет! Сегодня у тебя урок {lesson_number} — {lesson_title}. Готов продолжить обучение?")


def setup_reminders(bot: Bot) -> None:
    scheduler.remove_all_jobs()
    with SessionLocal() as db:
        users = list(db.scalars(select(User).where(User.reminder_time.is_not(None))).all())
        for u in users:
            if not u.reminder_time or not u.current_lesson_id:
                continue
            lesson = db.get(Lesson, u.current_lesson_id)
            if not lesson:
                continue
            hour, minute = map(int, u.reminder_time.split(":"))
            scheduler.add_job(send_daily_reminder, CronTrigger(hour=hour, minute=minute), kwargs={"bot": bot, "user_id": u.telegram_id, "lesson_title": lesson.title, "lesson_number": lesson.lesson_number}, id=f"reminder_{u.telegram_id}", replace_existing=True)
    if not scheduler.running:
        scheduler.start()
