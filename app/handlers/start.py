from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, FSInputFile, Message
from sqlalchemy import select

from app.content.welcome import WELCOME_TEXT, welcome_image_path
from app.keyboards.inline import (
    onboarding_ai_help_kb,
    onboarding_goal_kb,
    onboarding_learning_style_kb,
    onboarding_level_kb,
    onboarding_minutes_kb,
    onboarding_pace_kb,
    onboarding_practice_style_kb,
    onboarding_reminder_kb,
)
from app.models.user import User
from app.services.lesson_service import get_first_lesson
from database import SessionLocal

router = Router()


class OnboardingState(StatesGroup):
    daily_minutes = State()
    reminder_time = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()

    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == message.from_user.id))

        if user and user.level and user.goal:
            await message.answer(
                "👋 Ты уже зарегистрирован.\n\n"
                "Продолжай обучение:\n"
                "📚 /lessons — каталог уроков\n"
                "📊 /progress — прогресс\n\n"
                "Настройки позже можно будет изменить через /settings"
            )
            return

        if not user:
            first = get_first_lesson(db)
            user = User(
                telegram_id=message.from_user.id,
                current_lesson_id=first.id if first else None,
            )
            db.add(user)
            db.commit()

    kb = onboarding_level_kb()
    image = welcome_image_path()

    if image:
        await message.answer_photo(FSInputFile(str(image)), caption=WELCOME_TEXT, reply_markup=kb)
    else:
        await message.answer(WELCOME_TEXT, reply_markup=kb)


@router.callback_query(lambda c: c.data and c.data.startswith("ob_level:"))
async def onboarding_level(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.level = callback.data.split(":", 1)[1]
        db.commit()
    await callback.message.answer("Отлично. Какая цель обучения?", reply_markup=onboarding_goal_kb())
    await callback.answer()


# @router.callback_query(lambda c: c.data and c.data.startswith("ob_goal:"))
# async def onboarding_goal(callback: CallbackQuery) -> None:
#     with SessionLocal() as db:
#         user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
#         user.goal = callback.data.split(":", 1)[1]
#         db.commit()
#     await callback.message.answer("Выбери срок обучения:", reply_markup=onboarding_deadline_kb())
#     await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_level:"))
async def onboarding_level(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.level = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Зачем тебе Python?", reply_markup=onboarding_goal_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_goal:"))
async def onboarding_goal(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.goal = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Как тебе лучше объяснять материал?", reply_markup=onboarding_learning_style_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_learning:"))
async def onboarding_learning(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.learning_style = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Какие задачи тебе полезнее?", reply_markup=onboarding_practice_style_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_practice:"))
async def onboarding_practice(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.practice_style = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Как AI-помощник должен помогать?", reply_markup=onboarding_ai_help_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_ai:"))
async def onboarding_ai(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.ai_help_style = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Какой темп обучения выбрать?", reply_markup=onboarding_pace_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_pace:"))
async def onboarding_pace(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.pace = callback.data.split(":", 1)[1]
        db.commit()

    await callback.message.answer("Сколько минут в день готов заниматься?", reply_markup=onboarding_minutes_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_minutes:"))
async def onboarding_minutes(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.daily_minutes = int(callback.data.split(":", 1)[1])
        db.commit()

    await callback.message.answer("Когда напоминать о занятиях?", reply_markup=onboarding_reminder_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("ob_reminder:"))
async def onboarding_reminder(callback: CallbackQuery, state: FSMContext) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        user.reminder_time = callback.data.split(":", 1)[1]
        db.commit()

    await state.clear()
    await callback.message.answer(
        "✅ Готово! Я настроил обучение под тебя.\n\n"
        "Открой каталог уроков: /lessons\n"
        "Или посмотри прогресс: /progress"
    )
    await callback.answer()
