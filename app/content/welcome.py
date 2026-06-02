from pathlib import Path

from config import PROJECT_DIR

WELCOME_TEXT = """Привет! 👋

Я — твой персональный AI-планировщик изучения Python 🐍

Я помогу тебе пройти обучение по шагам:
📚 составлю персональный план;
🗓 буду выдавать урок на каждый день;
✏️ 5 практических задач и 🧪 5 вопросов теста в боте;
🤖 AI объяснит проще, ответит на вопросы и разберёт код;
🧪 буду проводить мини-тесты;
🔁 напомню, когда нужно повторить тему;
📊 покажу твой прогресс.

Обучение построено по темам курса Python: от установки интерпретатора и базового синтаксиса до функций, ООП, работы с файлами, JSON, pandas и requests.

Чтобы составить план, мне нужно немного узнать о тебе.

Начнём настройку? 🚀"""

WELCOME_IMAGE_NAMES = ("welcome.png", "welcome.jpg", "welcome.jpeg", "welcome.webp")


def welcome_image_path() -> Path | None:
    folder = PROJECT_DIR / "assets" / "welcome"
    for name in WELCOME_IMAGE_NAMES:
        path = folder / name
        if path.is_file():
            return path
    return None
