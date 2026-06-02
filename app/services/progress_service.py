from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.progress import UserProgress
from app.models.repetition import Repetition
from app.models.test_result import TestResult
from database import utcnow


def get_or_create_progress(db: Session, user_id: int, lesson_id: int) -> UserProgress:
    row = db.scalar(select(UserProgress).where(UserProgress.user_id == user_id, UserProgress.lesson_id == lesson_id))
    if row:
        return row
    row = UserProgress(user_id=user_id, lesson_id=lesson_id, status="in_progress")
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def update_tasks_progress(db: Session, user_id: int, lesson_id: int, solved_tasks: int, total_tasks: int) -> UserProgress:
    row = get_or_create_progress(db, user_id, lesson_id)
    row.solved_tasks = solved_tasks
    row.total_tasks = total_tasks
    row.status = "done" if solved_tasks >= total_tasks else "in_progress"
    if row.status == "done":
        row.completed_at = utcnow()
    db.commit()
    db.refresh(row)
    return row


def mark_completed(db: Session, user_id: int, lesson_id: int) -> UserProgress:
    row = get_or_create_progress(db, user_id, lesson_id)
    row.status = "done"
    row.completed_at = utcnow()
    db.commit()
    db.refresh(row)
    for d in (1, 3, 7):
        db.add(Repetition(user_id=user_id, lesson_id=lesson_id, repeat_date=date.today() + timedelta(days=d), interval_days=d, is_done=False))
    db.commit()
    return row


def save_test_result(db: Session, user_id: int, lesson_id: int, score: int, total_questions: int) -> None:
    db.add(TestResult(user_id=user_id, lesson_id=lesson_id, score=score, total_questions=total_questions))
    progress = get_or_create_progress(db, user_id, lesson_id)
    progress.test_score = round((score / total_questions) * 100, 2) if total_questions else 0
    db.commit()


def get_last_test_percent(db: Session, user_id: int, lesson_id: int) -> float | None:
    row = db.scalar(
        select(TestResult)
        .where(TestResult.user_id == user_id, TestResult.lesson_id == lesson_id)
        .order_by(TestResult.created_at.desc())
    )
    if not row or not row.total_questions:
        return None
    return round((row.score / row.total_questions) * 100, 2)


def build_user_progress_summary(db: Session, user_id: int) -> dict:
    rows = list(db.scalars(select(UserProgress).where(UserProgress.user_id == user_id)).all())
    done = sum(1 for r in rows if r.status == "done")
    solved = sum(r.solved_tasks for r in rows)
    total = sum(r.total_tasks for r in rows)
    percent = round((done / len(rows)) * 100, 2) if rows else 0
    tests = list(db.scalars(select(TestResult).where(TestResult.user_id == user_id).order_by(TestResult.created_at.desc()).limit(5)).all())
    return {"completed_lessons": done, "tracked_lessons": len(rows), "solved_tasks": solved, "total_tasks": total, "overall_percent": percent, "tests": tests}


def today_repetitions(db: Session, user_id: int) -> list[Repetition]:
    return list(db.scalars(select(Repetition).where(Repetition.user_id == user_id, Repetition.repeat_date == date.today(), Repetition.is_done.is_(False))).all())
