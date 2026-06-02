from app.services.reminder_service import setup_reminders


def start_scheduler(bot) -> None:
    setup_reminders(bot)
