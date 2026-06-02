from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, Message
from sqlalchemy import select

from app.keyboards.inline import lesson_menu_kb, lessons_list_kb
from app.models.user import User
from app.services.lesson_menu_service import LESSONS_LIST_TEXT, lesson_menu_text, send_lessons_list
from app.services.lesson_service import (
    get_lesson_by_id,
    get_lessons_with_status,
    get_next_lesson,
    load_lesson_images,
    load_lesson_text,
)
from app.services.telegram_format import sanitize_telegram_html, split_html_for_telegram
from app.services.progress_service import get_or_create_progress, mark_completed
from config import get_settings
from database import SessionLocal

router = Router()
settings = get_settings()


@router.message(Command("lessons"))
async def cmd_lessons_catalog(message: Message) -> None:
    await send_lessons_list(message, message.from_user.id)


@router.message(Command("today"))
async def cmd_today(message: Message) -> None:
    await send_lessons_list(
        message,
        message.from_user.id,
        header="📅 <b>Урок на сегодня</b>\n\nВыберите урок из списка или продолжите рекомендуемый:",
    )


@router.callback_query(lambda c: c.data == "lessons_list")
async def cb_lessons_list(callback: CallbackQuery) -> None:
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        if not user:
            await callback.answer("Сначала /start", show_alert=True)
            return
        items = get_lessons_with_status(db, user.id)
        current = get_lesson_by_id(db, user.current_lesson_id) if user.current_lesson_id else None
    text = LESSONS_LIST_TEXT
    if current:
        text += f"\n\n📌 Рекомендуемый: <b>{current.lesson_number}</b> — {current.title}"
    try:
        await callback.message.edit_text(text, reply_markup=lessons_list_kb(items), parse_mode="HTML")
    except Exception:
        await callback.message.answer(text, reply_markup=lessons_list_kb(items), parse_mode="HTML")
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("select:"))
async def select_lesson(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":", 1)[1])
    await state.update_data(context_lesson_id=lesson_id)
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        lesson = get_lesson_by_id(db, lesson_id)
        if not user or not lesson:
            await callback.answer("Урок не найден", show_alert=True)
            return
        status = get_or_create_progress(db, user.id, lesson.id).status
    text = lesson_menu_text(lesson.lesson_number, lesson.title, status)
    try:
        await callback.message.edit_text(text, reply_markup=lesson_menu_kb(lesson.id), parse_mode="HTML")
    except Exception:
        await callback.message.answer(text, reply_markup=lesson_menu_kb(lesson.id), parse_mode="HTML")
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("open:"))
async def open_lesson(callback: CallbackQuery, state: FSMContext) -> None:
    lesson_id = int(callback.data.split(":", 1)[1])
    await state.update_data(context_lesson_id=lesson_id)
    with SessionLocal() as db:
        lesson = get_lesson_by_id(db, lesson_id)
        if not lesson:
            await callback.message.answer("Урок не найден")
            await callback.answer()
            return
        try:
            text = load_lesson_text(settings.lessons_dir, lesson.path)
        except FileNotFoundError as e:
            await callback.message.answer(str(e))
            await callback.answer()
            return
        await callback.message.answer(f"Урок {lesson.lesson_number}: {lesson.title}")
        safe = sanitize_telegram_html(text)
        for chunk in split_html_for_telegram(safe):
            await callback.message.answer(chunk, parse_mode="HTML")
        for img in load_lesson_images(settings.lessons_dir, lesson.path):
            await callback.message.answer_photo(FSInputFile(str(img)))
        await callback.message.answer("Что сделать дальше?", reply_markup=lesson_menu_kb(lesson.id))
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("done:"))
async def mark_done(callback: CallbackQuery) -> None:
    lesson_id = int(callback.data.split(":", 1)[1])
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.telegram_id == callback.from_user.id))
        lesson = get_lesson_by_id(db, lesson_id)
        if not user or not lesson:
            await callback.message.answer("Не удалось отметить")
            await callback.answer()
            return
        mark_completed(db, user.id, lesson.id)
        nxt = get_next_lesson(db, lesson.order_index)
        if nxt:
            user.current_lesson_id = nxt.id
            db.commit()
        items = get_lessons_with_status(db, user.id)
    note = f"\n\nСледующий рекомендуемый: <b>{nxt.lesson_number}</b> — {nxt.title}" if nxt else "\n\n🎉 Все уроки в плане пройдены!"
    await callback.message.answer(
        f"✅ Урок <b>{lesson.lesson_number}</b> отмечен как выполненный!{note}\n\nВыберите любой урок:",
        reply_markup=lessons_list_kb(items),
        parse_mode="HTML",
    )
    await callback.answer()
