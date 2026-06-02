from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers import help as help_h
from app.handlers import ai, lessons, plan, progress, repeat, roadmap, start, tasks, tests, weaknesses
from app.services.lesson_service import seed_lessons_if_empty
from app.services.scheduler import start_scheduler
from config import get_settings
from database import SessionLocal, init_db


async def main() -> None:
    settings = get_settings()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=MemoryStorage())

    init_db()
    with SessionLocal() as db:
        seed_lessons_if_empty(db)

    dp.include_router(start.router)
    dp.include_router(lessons.router)
    dp.include_router(tasks.router)
    dp.include_router(tests.router)
    dp.include_router(ai.router)
    dp.include_router(progress.router)
    dp.include_router(plan.router)
    dp.include_router(repeat.router)
    dp.include_router(help_h.router)
    dp.include_router(roadmap.router)
    dp.include_router(weaknesses.router)

    start_scheduler(bot)
    await dp.start_polling(bot)
