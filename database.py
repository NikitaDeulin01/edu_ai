from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


def init_db() -> None:
    from app.models.user import User  # noqa: F401
    from app.models.lesson import Lesson  # noqa: F401
    from app.models.progress import UserProgress  # noqa: F401
    from app.models.test_result import TestResult  # noqa: F401
    from app.models.repetition import Repetition  # noqa: F401
    from app.models.user_mistake import UserMistake  # noqa: F401
    Base.metadata.create_all(bind=engine)


def utcnow() -> datetime:
    return datetime.utcnow()
