from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.models.lesson import Lesson
from config import get_settings

STATUS_ICONS = {
    "not_started": "⬜",
    "in_progress": "🟡",
    "done": "✅",
}


def _lesson_button_label(lesson: Lesson, status: str) -> str:
    icon = STATUS_ICONS.get(status, "⬜")
    label = f"{icon} {lesson.lesson_number} · {lesson.title}"
    if len(label) > 64:
        label = f"{icon} {lesson.lesson_number} · {lesson.title[:48]}…"
    return label


def lessons_list_kb(lessons_with_status: list[tuple[Lesson, str]]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for lesson, status in lessons_with_status:
        b.button(text=_lesson_button_label(lesson, status), callback_data=f"select:{lesson.id}")
    b.adjust(1)
    b.button(text="📊 Мой прогресс", callback_data="show_progress")
    return b.as_markup()


def lesson_menu_kb(lesson_id: int, *, show_extra_tasks: bool = False) -> InlineKeyboardMarkup:
    llm_enabled = get_settings().llm_enabled
    b = InlineKeyboardBuilder()
    b.button(text="📖 Читать урок", callback_data=f"open:{lesson_id}")
    b.button(text="🧪 Мини-тест (5 вопр.)", callback_data=f"test:{lesson_id}")
    b.button(text="✏️ Практика (5 задач)", callback_data=f"practice:{lesson_id}")
    if llm_enabled:
        b.button(text="❓ Объясни проще", callback_data=f"llm:explain:{lesson_id}")
        b.button(text="🐞 Разобрать код", callback_data=f"llm:debug:{lesson_id}")
        if show_extra_tasks:
            b.button(text="🧩 Доп. задачи (AI)", callback_data=f"llm:extra:{lesson_id}")
    b.button(text="✅ Урок пройден", callback_data=f"done:{lesson_id}")
    b.button(text="◀️ Все уроки", callback_data="lessons_list")
    b.adjust(1)
    return b.as_markup()

def onboarding_learning_style_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Простыми словами", callback_data="ob_learning:simple")
    b.button(text="С примерами из жизни", callback_data="ob_learning:examples")
    b.button(text="Коротко и по делу", callback_data="ob_learning:concise")
    b.adjust(1)
    return b.as_markup()


def onboarding_practice_style_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Пошаговые задачи", callback_data="ob_practice:step_by_step")
    b.button(text="Задачи с вызовом", callback_data="ob_practice:challenge")
    b.button(text="Мини-проекты", callback_data="ob_practice:projects")
    b.adjust(1)
    return b.as_markup()


def onboarding_ai_help_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Только подсказки", callback_data="ob_ai:hints")
    b.button(text="Разбирать ошибки", callback_data="ob_ai:debug")
    b.button(text="Показывать решение", callback_data="ob_ai:full_explain")
    b.adjust(1)
    return b.as_markup()


def onboarding_pace_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Спокойный", callback_data="ob_pace:calm")
    b.button(text="Обычный", callback_data="ob_pace:normal")
    b.button(text="Быстрый", callback_data="ob_pace:fast")
    b.adjust(1)
    return b.as_markup()


def onboarding_minutes_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="15 минут", callback_data="ob_minutes:15")
    b.button(text="30 минут", callback_data="ob_minutes:30")
    b.button(text="60 минут", callback_data="ob_minutes:60")
    b.adjust(3)
    return b.as_markup()


def onboarding_reminder_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Утром", callback_data="ob_reminder:09:00")
    b.button(text="Днём", callback_data="ob_reminder:14:00")
    b.button(text="Вечером", callback_data="ob_reminder:19:00")
    b.adjust(3)
    return b.as_markup()

def task_practice_kb(lesson_id: int, task_idx: int) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="💡 Подсказка", callback_data=f"thint:{lesson_id}:{task_idx}")
    b.button(text="📋 Показать ответ", callback_data=f"tsol:{lesson_id}:{task_idx}")
    b.button(text="✅ Я решил", callback_data=f"tsolved:{lesson_id}:{task_idx}")
    b.button(text="⏭ Пропустить", callback_data=f"tskip:{lesson_id}:{task_idx}")
    b.adjust(2, 2)
    return b.as_markup()


def task_choice_kb(lesson_id: int, task_idx: int, options: list[str]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for idx, opt in enumerate(options):
        b.button(text=opt, callback_data=f"tchk:{lesson_id}:{task_idx}:{idx}")
    b.button(text="⏭ Пропустить", callback_data=f"tskip:{lesson_id}:{task_idx}")
    b.adjust(1)
    return b.as_markup()


def onboarding_level_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Новичок", callback_data="ob_level:beginner")
    b.button(text="Немного знаю Python", callback_data="ob_level:some")
    b.button(text="Уже программировал", callback_data="ob_level:pro")
    b.adjust(1)
    return b.as_markup()


def onboarding_goal_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="Пройти курс", callback_data="ob_goal:course")
    b.button(text="Подготовиться к экзамену", callback_data="ob_goal:exam")
    b.button(text="Научиться писать проекты", callback_data="ob_goal:projects")
    b.adjust(1)
    return b.as_markup()


def onboarding_deadline_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="1 месяц", callback_data="ob_deadline:1")
    b.button(text="2 месяца", callback_data="ob_deadline:2")
    b.button(text="3 месяца", callback_data="ob_deadline:3")
    b.adjust(3)
    return b.as_markup()


def stepik_progress_kb(lesson_id: int) -> InlineKeyboardMarkup:
    return lesson_menu_kb(lesson_id)


def test_options_kb(lesson_id: int, q_idx: int, options: list[str]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for idx, opt in enumerate(options):
        b.button(text=opt, callback_data=f"tans:{lesson_id}:{q_idx}:{idx}")
    b.adjust(1)
    return b.as_markup()


