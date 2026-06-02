import html
from collections import defaultdict

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from app.models.lesson import Lesson
from app.models.user import User
from app.models.user_mistake import UserMistake
from app.services.llm_service import LLMNotConfiguredError, LLMRequestError, chat
from datetime import datetime, timedelta
from database import SessionLocal

router = Router()


@router.message(Command("weaknesses"))
async def cmd_weaknesses(message: Message) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == message.from_user.id))

        if not user:
            await message.answer("Сначала /start")
            return

        rows = db.execute(
            select(UserMistake, Lesson)
            .join(Lesson, UserMistake.lesson_id == Lesson.id, isouter=True)
            .where(
                UserMistake.user_id == user.id,
                UserMistake.created_at >= datetime.utcnow() - timedelta(days=21)
            )
            .order_by(UserMistake.created_at.desc())
            .limit(30)
        ).all()

    if not rows:
        await message.answer("🧠 Пока проблемных мест не найдено 👍")
        return

    by_module = defaultdict(list)

    for mistake, lesson in rows:
        module_number = lesson.module_number if lesson else 0
        lesson_title = lesson.title if lesson else "Без урока"
        lesson_number = lesson.lesson_number if lesson else "-"

        by_module[module_number].append(
            {
                "lesson_number": lesson_number,
                "lesson_title": lesson_title,
                "topic": mistake.topic,
                "description": mistake.description,
                "source": mistake.source,
            }
        )

    text = "🧠 <b>Проблемные места</b>\n\n"

    for module_number, mistakes in sorted(by_module.items()):
        module_name = f"Модуль {module_number}" if module_number else "Без модуля"
        text += f"📦 <b>{module_name}</b>\n"
        text += f"Пробелов найдено: <b>{len(mistakes)}</b>\n"

        lesson_counts = defaultdict(int)
        for item in mistakes:
            lesson_counts[f"{item['lesson_number']} — {item['lesson_title']}"] += 1

        for lesson_name, count in lesson_counts.items():
            text += f"• {html.escape(lesson_name)}: {count}\n"

        text += "\n"

    llm_input = "\n".join(
        [
            f"Модуль {lesson.module_number if lesson else '-'}, "
            f"урок {lesson.lesson_number if lesson else '-'} — {lesson.title if lesson else 'Без урока'}\n"
            f"Тема ошибки: {mistake.topic}\n"
            f"Описание: {mistake.description}\n"
            for mistake, lesson in rows[:20]
        ]
    )

    wait = await message.answer("⏳ AI-учитель анализирует пробелы...")

    system = (
        "Ты AI-учитель Python. "
        "Проанализируй ошибки ученика и сделай короткую педагогическую сводку. "
        "Пиши по-русски, дружелюбно, конкретно. "
        "Не перечисляй все ошибки подряд. "
        "Сгруппируй проблемы по смыслу. "
        "Дай 3–5 рекомендаций, что повторить. "
        "Форматируй для Telegram HTML. "
        "Используй только теги <b>, <i>, <code>. "
        "Не используй Markdown."
    )

    user_prompt = f"""
Вот ошибки и пропуски ученика:

{llm_input}

Сделай блок:
<b>Мнение AI-учителя</b>

Нужно:
1. Кратко сказать, какие темы проседают.
2. Объяснить вероятную причину.
3. Дать конкретный план повторения.
4. Не ругать ученика.
5. Не перечислять все ошибки подряд.
"""

    try:
        ai_summary = await chat(
            system=system,
            user=user_prompt,
            temperature=0.4,
            max_tokens=1200,
        )
    except (LLMNotConfiguredError, LLMRequestError):
        ai_summary = (
            "<b>Мнение AI-учителя</b>\n\n"
            "Пока не удалось получить AI-сводку. Но по статистике выше уже видно, "
            "какие модули стоит повторить."
        )

    await wait.delete()

    final_text = text + "\n" + ai_summary
    await message.answer(final_text, parse_mode="HTML")