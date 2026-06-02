from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from sqlalchemy import select

from app.models.user import User
from app.services.llm_service import LLMNotConfiguredError, LLMRequestError, chat
from app.services.telegram_format import answer_html
from database import SessionLocal

router = Router()


class RoadmapState(StatesGroup):
    waiting_goal = State()


@router.message(Command("roadmap"))
async def cmd_roadmap(message: Message, state: FSMContext) -> None:
    await state.set_state(RoadmapState.waiting_goal)
    await message.answer(
        "🧭 <b>Персональный roadmap</b>\n\n"
        "Напиши своими словами, для чего тебе Python.\n\n"
        "Например:\n"
        "• хочу стать backend-разработчиком\n"
        "• хочу делать Telegram-ботов\n"
        "• хочу заниматься AI и нейросетями\n"
        "• хочу автоматизировать работу\n"
        "• хочу писать игры\n\n"
        "Ответь одним сообщением.",
        parse_mode="HTML",
    )


@router.message(RoadmapState.waiting_goal)
async def process_roadmap_goal(message: Message, state: FSMContext) -> None:
    goal = (message.text or "").strip()

    if len(goal) < 5:
        await message.answer("Напиши чуть подробнее: кем хочешь стать или что хочешь делать на Python?")
        return

    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == message.from_user.id))

    system = (
        "Ты карьерный наставник по Python и методист онлайн-курса. "
        "Твоя задача — построить персональный roadmap обучения по Python. "
        "Пиши по-русски, понятно, структурно, без воды. "
        "Учитывай уровень пользователя, цель и темп. "
        "Не делай слишком длинный ответ. "
        "Форматируй под Telegram: заголовки, списки, эмодзи. "
        "Не используй Markdown-таблицы."
    )

    user_prompt = f"""
Пользователь написал цель своими словами:
{goal}

Профиль пользователя:
- уровень: {user.level if user else "неизвестен"}
- цель из анкеты: {user.goal if user else "неизвестна"}
- стиль объяснений: {user.learning_style if user else "неизвестен"}
- стиль практики: {user.practice_style if user else "неизвестен"}
- темп: {user.pace if user else "неизвестен"}
- минут в день: {user.daily_minutes if user else "неизвестно"}

Составь roadmap:

1. Кратко объясни, насколько цель реалистична.
2. Разбей путь на 5–7 этапов.
3. Для каждого этапа укажи:
   - что изучать;
   - какие технологии добавить;
   - какой мини-проект сделать.
4. Отдельно дай список технологий вокруг Python.
5. Дай 3 идеи проектов в портфолио.
6. Заверши советом: с чего начать прямо сейчас.

Важно:
- не обещай точные сроки трудоустройства;
- не перегружай новичка;
- если цель размытая, предложи 2–3 возможных направления.
"""

    await state.clear()
    wait = await message.answer("⏳ Строю твой roadmap...")

    try:
        result = await chat(
            system=system,
            user=user_prompt,
            temperature=0.6,
            max_tokens=2500,
        )
    except LLMNotConfiguredError as e:
        await wait.edit_text(str(e))
        return
    except LLMRequestError as e:
        await wait.edit_text(f"Ошибка LLM: {e}")
        return

    await wait.delete()
    await answer_html(message, result)