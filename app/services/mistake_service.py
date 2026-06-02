from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.user_mistake import UserMistake


def add_user_mistake(
    db: Session,
    *,
    user_id: int,
    lesson_id: int | None,
    source: str,
    topic: str,
    description: str,
) -> UserMistake:
    mistake = UserMistake(
        user_id=user_id,
        lesson_id=lesson_id,
        source=source,
        topic=topic[:128],
        description=description,
    )
    db.add(mistake)
    db.commit()
    db.refresh(mistake)
    return mistake


def get_recent_user_mistakes(
    db: Session,
    user_id: int,
    limit: int = 5,
) -> list[UserMistake]:
    return list(
        db.scalars(
            select(UserMistake)
            .where(UserMistake.user_id == user_id)
            .order_by(desc(UserMistake.created_at))
            .limit(limit)
        ).all()
    )


def build_mistakes_prompt(db: Session, user_id: int) -> str:
    mistakes = get_recent_user_mistakes(db, user_id)

    if not mistakes:
        return "Недавних ошибок пользователя пока нет."

    lines = ["Недавние слабые места пользователя:"]
    for mistake in mistakes:
        lines.append(f"- {mistake.topic}: {mistake.description}")

    return "\n".join(lines)