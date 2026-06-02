from aiogram.types import Message

from app.keyboards.inline import lesson_menu_kb, lessons_list_kb
from app.models.user import User
from app.services.lesson_service import get_lesson_by_id, get_lessons_with_status
from database import SessionLocal
from sqlalchemy import select

LESSONS_LIST_TEXT = (
    "📚 <b>Каталог уроков</b>\n\n"
    "Нажмите на любой урок — откроется меню с действиями.\n\n"
    "⬜ не начат   🟡 в процессе   ✅ выполнен"
)

STATUS_LABELS = {
    "not_started": "не начат",
    "in_progress": "в процессе",
    "done": "выполнен",
}


def lesson_menu_text(lesson_number: str, title: str, status: str) -> str:
    human = STATUS_LABELS.get(status, status)
    return f"<b>Урок {lesson_number}</b>\n{title}\n\nСтатус: {human}"


async def send_lessons_list(message: Message, telegram_id: int, *, header: str | None = None) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            await message.answer("Сначала /start")
            return

        items = get_lessons_with_status(db, user.id)
        current = get_lesson_by_id(db, user.current_lesson_id) if user.current_lesson_id else None

        text = header or LESSONS_LIST_TEXT

        if current and header:
            text = f"{header}\n\n📌 Рекомендуемый: <b>{current.lesson_number}</b> — {current.title}"
        elif current and not header:
            text = (
                f"{LESSONS_LIST_TEXT}\n\n"
                f"📌 Рекомендуемый урок: <b>{current.lesson_number}</b> — {current.title}"
            )

        keyboard = lessons_list_kb(items)

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")


def lesson_menu_markup(lesson_id: int):
    return lesson_menu_kb(lesson_id)
