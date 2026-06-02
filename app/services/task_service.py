import json
import re
from pathlib import Path

from app.services.llm_service import LLMNotConfiguredError, LLMRequestError, chat


def load_tasks_file(tasks_dir: str, lesson_number: str) -> list[dict]:
    file_name = f"lesson_{lesson_number.replace('.', '_')}.json"
    path = Path(tasks_dir) / file_name
    if not path.exists():
        raise FileNotFoundError(f"Задачи не найдены: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("tasks", [])
    return data


async def check_task_answer(task: dict, answer: str) -> tuple[bool, str]:
    task_type = task.get("type", "text")
    normalized = answer.strip()

    if task_type == "choice":
        return False, "Ответьте кнопкой с вариантом"

    hard_ok, hard_feedback = _hard_check_task_answer(task, normalized)

    if hard_ok:
        return True, hard_feedback

    if task.get("use_llm_check"):
        return await _llm_check_task_answer(task, normalized, hard_feedback)

    return False, hard_feedback


def _hard_check_task_answer(task: dict, normalized: str) -> tuple[bool, str]:
    task_type = task.get("type", "text")

    if task_type == "code":
        lower = normalized.lower()
        required = [s.lower() for s in task.get("check_contains", [])]

        if required and all(token in lower for token in required):
            return True, task.get("explanation", "Верно!")

        if normalized == task.get("solution", "").strip():
            return True, task.get("explanation", "Верно!")

        return False, task.get("hint", "Проверьте синтаксис и условие задачи")

    acceptable = task.get("acceptable_answers", [])
    norm_answers = [_normalize(a) for a in acceptable]

    if _normalize(normalized) in norm_answers:
        return True, task.get("explanation", "Верно!")

    return False, task.get("hint", "Попробуйте ещё раз")


async def _llm_check_task_answer(task: dict, answer: str, fallback_feedback: str) -> tuple[bool, str]:
    system = (
        "Ты проверяешь учебную задачу по Python для начинающего ученика.\n"
        "Твоя задача — понять, решает ли ответ ученика поставленную задачу по смыслу.\n\n"
        "Правила:\n"
        "- Будь строгим к логике, но не придирайся к форматированию без причины.\n"
        "- Если код в целом решает задачу — засчитай.\n"
        "- Если есть важная ошибка — не засчитывай.\n"
        "- Не давай длинный ответ.\n"
        "- Верни строго один из форматов:\n"
        "OK|||короткий комментарий\n"
        "FAIL|||короткое объяснение ошибки"
    )

    user = f"""
ЗАДАЧА:
{task.get("question", "-")}

ТИП ЗАДАЧИ:
{task.get("type", "text")}

ЭТАЛОННОЕ РЕШЕНИЕ:
{task.get("solution", "-")}

ПОДСКАЗКА:
{task.get("hint", "-")}

ОБЪЯСНЕНИЕ:
{task.get("explanation", "-")}

ОТВЕТ УЧЕНИКА:
{answer}
""".strip()

    try:
        result = await chat(
            system=system,
            user=user,
            temperature=0.1,
            max_tokens=300,
        )
    except (LLMNotConfiguredError, LLMRequestError):
        return False, fallback_feedback

    result = result.strip()

    if result.startswith("OK|||"):
        feedback = result.split("|||", 1)[1].strip()
        return True, feedback or task.get("explanation", "Верно!")

    if result.startswith("FAIL|||"):
        feedback = result.split("|||", 1)[1].strip()
        return False, feedback or fallback_feedback

    return False, fallback_feedback


def _normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())