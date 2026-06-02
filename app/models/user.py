from sqlalchemy import BigInteger, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, utcnow


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True)
    level: Mapped[str | None] = mapped_column(String(64), nullable=True)
    goal: Mapped[str | None] = mapped_column(String(128), nullable=True)
    learning_style: Mapped[str | None] = mapped_column(String(64), nullable=True)
    practice_style: Mapped[str | None] = mapped_column(String(64), nullable=True)
    ai_help_style: Mapped[str | None] = mapped_column(String(64), nullable=True)
    pace: Mapped[str | None] = mapped_column(String(64), nullable=True)
    deadline_months: Mapped[int | None] = mapped_column(Integer, nullable=True)
    daily_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    reminder_time: Mapped[str | None] = mapped_column(String(5), nullable=True)
    current_lesson_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=utcnow, nullable=False)
    
