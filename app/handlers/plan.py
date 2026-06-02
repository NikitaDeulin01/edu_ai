from aiogram import Router
from aiogram.filters import Command

from app.services.lesson_menu_service import send_lessons_list

router = Router()


@router.message(Command("plan"))
async def cmd_plan(message):
    await send_lessons_list(message, message.from_user.id)
