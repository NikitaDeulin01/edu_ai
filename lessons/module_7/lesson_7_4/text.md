<b>🧪 Урок 7.4. Введение в Pytest</b>

<i>Любая программа рано или поздно начинает расти. Чем больше кода, тем выше шанс случайно что-то сломать. Именно поэтому профессиональные разработчики используют автоматические тесты. Самая популярная библиотека тестирования в Python называется Pytest.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое тестирование</b>

Представьте, что вы написали функцию:

<pre><code class="language-python">def add(a, b):
    return a + b</code></pre>

Сегодня она работает правильно.

Но через месяц вы изменили код.

Как убедиться, что функция всё ещё работает?

Можно проверять вручную:

<pre><code class="language-python">print(add(2, 3))</code></pre>

Но это неудобно.

Для таких случаев существуют тесты.

━━━━━━━━━━━

Тест — это код, который автоматически проверяет другой код.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Что такое Pytest</b>

<b>Pytest</b> — самая популярная библиотека тестирования для Python.
Она позволяет:
• проверять функции
• проверять классы
• находить ошибки автоматически
• запускать сотни тестов одной командой
• контролировать качество проекта

━━━━━━━━━━━

Pytest используется практически во всех серьёзных Python-проектах.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Установка Pytest</b>

Установка:

<pre><code class="language-bash">pip install pytest</code></pre>

Проверка:

<pre><code class="language-bash">pytest --version</code></pre>

Пример:

<pre><code>pytest 8.2.0</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Первый тест</b>

Создадим файл:

<pre><code>calculator.py</code></pre>

Код:

<pre><code class="language-python">def add(a, b):
    return a + b</code></pre>

━━━━━━━━━━━

Создадим файл:

<pre><code>test_calculator.py</code></pre>

Тест:

<pre><code class="language-python">from calculator import add

def test_add():
    assert add(2, 3) == 5</code></pre>

━━━━━━━━━━━

Запуск:

<pre><code class="language-bash">pytest</code></pre>

Результат:

<pre><code>1 passed</code></pre>

Тест успешно прошёл.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Что такое assert</b>

Главный инструмент тестирования:

<pre><code class="language-python">assert</code></pre>

Он проверяет условие.

━━━━━━━━━━━

Пример:

<pre><code class="language-python">assert 2 + 2 == 4</code></pre>

Всё хорошо.

━━━━━━━━━━━

Пример ошибки:

<pre><code class="language-python">assert 2 + 2 == 5</code></pre>

Результат:

<pre><code>AssertionError</code></pre>

━━━━━━━━━━━

Если условие истинно — тест проходит.

Если ложно — тест падает.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Имена тестов</b>

Pytest автоматически ищет:

Файлы:

<pre><code>test_*.py</code></pre>

или

<pre><code>*_test.py</code></pre>

━━━━━━━━━━━

Функции:

<pre><code class="language-python">def test_something():
    ...</code></pre>

Если имя не начинается с <code>test_</code>, Pytest его не увидит.

━━━━━━━━━━━
<b>ЧАСТЬ 7. Несколько тестов</b>

Пример:

<pre><code class="language-python">from calculator import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(5, 0) == 5</code></pre>

Запуск:

<pre><code class="language-bash">pytest</code></pre>

Результат:

<pre><code>3 passed</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Когда тест падает</b>

Представим ошибку.

Функция:

<pre><code class="language-python">def add(a, b):
    return a - b</code></pre>

Тест:

<pre><code class="language-python">def test_add():
    assert add(2, 3) == 5</code></pre>

Pytest покажет:

<pre><code>E assert -1 == 5</code></pre>

Он сразу укажет место ошибки.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Проверка строк</b>

Пример:

<pre><code class="language-python">def greet(name):
    return f"Привет, {name}"</code></pre>

Тест:

<pre><code class="language-python">def test_greet():
    assert greet("Анна") == "Привет, Анна"</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Проверка списков</b>

Функция:

<pre><code class="language-python">def get_numbers():
    return [1, 2, 3]</code></pre>

Тест:

<pre><code class="language-python">def test_numbers():
    assert get_numbers() == [1, 2, 3]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Проверка исключений</b>

Иногда нужно проверить ошибку.

Функция:

<pre><code class="language-python">def divide(a, b):
    return a / b</code></pre>

Тест:

<pre><code class="language-python">import pytest

def test_divide_by_zero():

    with pytest.raises(
        ZeroDivisionError
    ):
        divide(10, 0)</code></pre>

━━━━━━━━━━━

Тест пройдёт только если действительно возникнет:

<pre><code>ZeroDivisionError</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Фикстуры (Fixtures)</b>

Одна из самых мощных возможностей Pytest.

Фикстура помогает подготовить данные для тестов.

Пример:

<pre><code class="language-python">import pytest

@pytest.fixture
def user_name():
    return "Иван"</code></pre>

Использование:

<pre><code class="language-python">def test_name(user_name):
    assert user_name == "Иван"</code></pre>

━━━━━━━━━━━

Фикстуры позволяют не дублировать код.

━━━━━━━━━━━
<b>ЧАСТЬ 13. Параметризация тестов</b>

Иногда нужно проверить функцию на многих значениях.

Пример:

<pre><code class="language-python">import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (10, 5, 15),
        (1, 1, 2)
    ]
)
def test_add(a, b, result):
    assert add(a, b) == result</code></pre>

━━━━━━━━━━━

Pytest создаст несколько тестов автоматически.

━━━━━━━━━━━
<b>ЧАСТЬ 14. Запуск конкретного файла</b>

Запустить один файл:

<pre><code class="language-bash">pytest test_calculator.py</code></pre>

━━━━━━━━━━━

Запустить конкретный тест:

<pre><code class="language-bash">pytest -k add</code></pre>

━━━━━━━━━━━

Запустить подробно:

<pre><code class="language-bash">pytest -v</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 15. Структура проекта</b>

Часто тесты выносят отдельно.

Пример:

<pre><code>project/

├── app.py
├── calculator.py

└── tests/
    ├── test_calculator.py
    └── test_user.py</code></pre>

Так проект становится чище.

━━━━━━━━━━━
<b>ЧАСТЬ 16. Почему тесты важны</b>

Без тестов:

❌ приходится всё проверять вручную

❌ ошибки легко пропустить

❌ страшно менять код

━━━━━━━━━━━
С тестами:
✅ быстро находятся ошибки
✅ безопаснее делать изменения
✅ проще поддерживать проект
✅ выше качество программы

━━━━━━━━━━━
<b>ЧАСТЬ 17. Где используется Pytest</b>

Pytest используется:
• Backend-разработка
• Telegram-боты
• Веб-приложения
• FastAPI
• Django
• Data Science
• Машинное обучение
• Автоматизация

━━━━━━━━━━━

Практически каждый серьёзный Python-проект имеет тесты.

━━━━━━━━━━━
<b>ЧАСТЬ 18. Типичные ошибки новичков</b>

<b>❌ Забывают установить Pytest</b>

Ошибка:

<pre><code>ModuleNotFoundError:
No module named pytest</code></pre>

Решение:

<pre><code class="language-bash">pip install pytest</code></pre>

━━━━━━━━━━━

<b>❌ Неправильное имя файла</b>

Pytest не найдёт:

<pre><code>calculator_tests.py</code></pre>

Лучше:

<pre><code>test_calculator.py</code></pre>

━━━━━━━━━━━

<b>❌ Неправильное имя функции</b>

Pytest не увидит:

<pre><code class="language-python">def check_add():
    pass</code></pre>

Правильно:

<pre><code class="language-python">def test_add():
    pass</code></pre>

━━━━━━━━━━━

<b>❌ Используют print вместо тестов</b>

Плохо:

<pre><code class="language-python">print(add(2, 3))</code></pre>

Лучше:

<pre><code class="language-python">assert add(2, 3) == 5</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• Pytest — самая популярная библиотека тестирования Python
• тесты автоматически проверяют код
• assert используется для проверки результата
• файлы тестов обычно начинаются с test_
• функции тестов начинаются с test_
• pytest умеет проверять исключения через raises()
• фикстуры помогают переиспользовать код
• параметризация позволяет запускать один тест на разных данных
• тесты помогают безопасно развивать проект
• хороший разработчик пишет не только код, но и тесты