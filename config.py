from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent
REPO_DIR = PROJECT_DIR.parent

def _load_env() -> None:
    """Подхватывает project/.env без BOM; override — актуальный файл важнее os.environ."""
    for path in (PROJECT_DIR / ".env", REPO_DIR / "project" / ".env"):
        if path.is_file():
            load_dotenv(path, encoding="utf-8-sig", override=True)


_load_env()


@dataclass(slots=True)
class Settings:
    bot_token: str
    database_url: str
    lessons_dir: str
    tests_dir: str
    tasks_dir: str
    tz: str
    llm_api_key: str
    llm_base_url: str
    llm_model: str
    llm_enabled: bool


def get_settings() -> Settings:
    token = os.getenv("BOT_TOKEN", "")
    if not token:
        raise ValueError("BOT_TOKEN is not set in project/.env")
    llm_key = os.getenv("LLM_API_KEY", "").strip()
    return Settings(
        bot_token=token,
        database_url=os.getenv("DATABASE_URL", "sqlite:///project/db.sqlite3"),
        lessons_dir=os.getenv("LESSONS_DIR", "project/lessons"),
        tests_dir=os.getenv("TESTS_DIR", "project/tests"),
        tasks_dir=os.getenv("TASKS_DIR", "project/tasks"),
        tz=os.getenv("TZ", "Europe/Moscow"),
        llm_api_key=llm_key,
        llm_base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/"),
        llm_model=os.getenv("LLM_MODEL", "gpt-oss-120b"),
        llm_enabled=bool(llm_key),
    )
