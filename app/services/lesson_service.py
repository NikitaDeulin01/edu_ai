import os
from pathlib import Path

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.services.lesson_catalog import LESSON_SEEDS
from app.services.progress_service import get_or_create_progress

TELEGRAM_TEXT_LIMIT = 3800


def seed_lessons_if_empty(db: Session) -> None:
    count = db.scalar(select(func.count(Lesson.id)))
    if count and count > 0:
        return
    for i, row in enumerate(LESSON_SEEDS, start=1):
        db.add(Lesson(module_number=row.module_number, lesson_number=row.lesson_number, title=row.title, path=row.path, total_tasks=row.total_tasks, order_index=i))
    db.commit()


def get_lesson_by_id(db: Session, lesson_id: int) -> Lesson | None:
    return db.get(Lesson, lesson_id)


def get_first_lesson(db: Session) -> Lesson | None:
    return db.scalar(select(Lesson).order_by(Lesson.order_index.asc()))


def get_next_lesson(db: Session, current_order: int) -> Lesson | None:
    return db.scalar(select(Lesson).where(Lesson.order_index == current_order + 1))


def get_all_lessons(db: Session) -> list[Lesson]:
    return list(db.scalars(select(Lesson).order_by(Lesson.order_index.asc())).all())


def get_lessons_with_status(db: Session, user_id: int) -> list[tuple[Lesson, str]]:
    return [(lesson, get_or_create_progress(db, user_id, lesson.id).status) for lesson in get_all_lessons(db)]


def split_for_telegram(text: str, limit: int = TELEGRAM_TEXT_LIMIT) -> list[str]:
    if len(text) <= limit:
        return [text]
    chunks, current, cur_len = [], [], 0
    for line in text.splitlines(keepends=True):
        if cur_len + len(line) > limit:
            chunks.append("".join(current).strip())
            current, cur_len = [line], len(line)
        else:
            current.append(line)
            cur_len += len(line)
    if current:
        chunks.append("".join(current).strip())
    return [c for c in chunks if c]


def load_lesson_text(lessons_dir: str, lesson_path: str) -> str:
    path = Path(lessons_dir) / lesson_path / "text.md"
    if not path.exists():
        raise FileNotFoundError(f"Не найден файл урока: {path}")
    return path.read_text(encoding="utf-8")


def load_lesson_images(lessons_dir: str, lesson_path: str) -> list[Path]:
    img_dir = Path(lessons_dir) / lesson_path / "images"
    if not img_dir.exists():
        return []
    return [img_dir / n for n in sorted(os.listdir(img_dir)) if n.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
