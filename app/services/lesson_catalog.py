from dataclasses import dataclass


@dataclass(frozen=True)
class LessonSeed:
    module_number: int
    lesson_number: str
    title: str
    path: str
    total_tasks: int


LESSON_SEEDS: list[LessonSeed] = [
    LessonSeed(1, "1.1", "Прежде чем начать", "module_1/lesson_1_1", 5),
    LessonSeed(1, "1.2", "Задачи, тесты и AI-помощник", "module_1/lesson_1_2", 5),
    LessonSeed(1, "1.3", "Введение в программирование", "module_1/lesson_1_3", 5),
    LessonSeed(1, "1.4", "Переменные и типы данных", "module_1/lesson_1_4", 5),
    LessonSeed(1, "1.5", "Базовые типы данных", "module_1/lesson_1_5", 5),
    LessonSeed(2, "2.1", "Ввод и вывод данных", "module_2/lesson_2_1", 5),
    LessonSeed(2, "2.2", "Типы данных в Python", "module_2/lesson_2_2", 5),
    LessonSeed(2, "2.3", "Преобразование типов и работа с вводом", "module_2/lesson_2_3", 5),
    LessonSeed(3, "3.1", "Условные операторы", "module_3/lesson_3_1", 5),
    LessonSeed(3, "3.2", "Циклы", "module_3/lesson_3_2", 5),
    LessonSeed(4, "4.1", "Создание и вызов функций", "module_4/lesson_4_1", 5),
    LessonSeed(4, "4.2", "Параметры, аргументы и return", "module_4/lesson_4_2", 5),
    LessonSeed(4, "4.3", "Практика работы с функциями", "module_4/lesson_4_3", 5),
    LessonSeed(4, "4.4", "Область видимости: Local, Global, Built-in и nonlocal", "module_4/lesson_4_4", 5),
    LessonSeed(4, "4.5", "Анонимные функции (lambda)", "module_4/lesson_4_5", 5),
    LessonSeed(5, "5.1", "Обработка исключений", "module_5/lesson_5_1", 5),
    LessonSeed(6, "6.1", "Классы и объекты", "module_6/lesson_6_1", 5),
    LessonSeed(6, "6.2", "Атрибуты, методы и инкапсуляция", "module_6/lesson_6_2", 5),
    LessonSeed(6, "6.3", "Наследование и полиморфизм", "module_6/lesson_6_3", 5),
    LessonSeed(7, "7.1", "NumPy", "module_7/lesson_7_1", 5),
    LessonSeed(7, "7.2", "Pandas", "module_7/lesson_7_2", 5),
    LessonSeed(7, "7.3", "Matplotlib", "module_7/lesson_7_3", 5),
    LessonSeed(7, "7.4", "Pytest", "module_7/lesson_7_4", 5),
    LessonSeed(7, "7.5", "Парсинг сайтов", "module_7/lesson_7_5", 5),
]
