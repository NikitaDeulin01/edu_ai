from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "/start — настройка\n"
        "/lessons или /plan — каталог уроков\n"
        "/today — урок дня + выбор любого урока\n"
        "/ask — вопрос по теме (нужен выбранный урок)\n"
        "/debug — разбор кода\n"
        "/progress — прогресс\n"
        "/repeat — повторение\n"
        "/help\n\n"
        "В меню урока: практика (5 задач), мини-тест (5 вопросов), AI-кнопки."
    )
