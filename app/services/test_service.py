import json
from pathlib import Path


def load_test_file(tests_dir: str, lesson_number: str) -> list[dict]:
    file_name = f"lesson_{lesson_number.replace('.', '_')}.json"
    path = Path(tests_dir) / file_name
    if not path.exists():
        raise FileNotFoundError(f"Тест не найден: {path}")
    return json.loads(path.read_text(encoding="utf-8"))
