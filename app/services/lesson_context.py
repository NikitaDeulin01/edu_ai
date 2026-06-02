from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.services.lesson_service import get_lesson_by_id, load_lesson_text
from app.services.telegram_format import html_to_plain_for_llm
from config import get_settings

settings = get_settings()
MAX_CONTEXT_CHARS = 12000


def get_lesson_context(db: Session, lesson_id: int) -> tuple[Lesson, str]:
    lesson = get_lesson_by_id(db, lesson_id)
    if not lesson:
        raise ValueError("Урок не найден")
    text = load_lesson_text(settings.lessons_dir, lesson.path)
    text = html_to_plain_for_llm(text)
    if len(text) > MAX_CONTEXT_CHARS:
        text = text[:MAX_CONTEXT_CHARS] + "\n\n[...текст урока сокращён для LLM...]"
    return lesson, text


def lesson_header(lesson: Lesson) -> str:
    return f"Урок {lesson.lesson_number}: {lesson.title}"
