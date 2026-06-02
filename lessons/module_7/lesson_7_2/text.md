<b>🐼 Урок 7.2. Введение в Pandas</b>

<i>NumPy отлично подходит для вычислений, но когда нужно работать с таблицами, CSV-файлами, Excel и реальными данными — используется Pandas. Это одна из самых популярных библиотек в мире Data Science и аналитики данных.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое Pandas</b>

<b>Pandas</b> — это библиотека для обработки и анализа табличных данных.

С её помощью можно:
• читать CSV-файлы
• работать с Excel
• фильтровать данные
• искать информацию
• группировать данные
• анализировать статистику
• подготавливать данные для машинного обучения

━━━━━━━━━━━

Pandas используется практически в каждом проекте по анализу данных.

Она построена поверх NumPy.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Установка Pandas</b>

Установка через pip:

<pre><code class="language-bash">pip install pandas</code></pre>

Импорт:

<pre><code class="language-python">import pandas as pd</code></pre>

Сокращение <code>pd</code> используется практически во всех проектах.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Основные объекты Pandas</b>

В Pandas есть два главных типа данных:

<b>Series</b>

и

<b>DataFrame</b>

━━━━━━━━━━━

<b>Series</b> — это один столбец данных.

Пример:

<pre><code class="language-python">import pandas as pd

ages = pd.Series([18, 21, 25, 30])

print(ages)</code></pre>

Результат:

<pre><code>0    18
1    21
2    25
3    30
dtype: int64</code></pre>

━━━━━━━━━━━

Каждый элемент имеет индекс.

По сути Series напоминает улучшенный список.

━━━━━━━━━━━
<b>ЧАСТЬ 4. Что такое DataFrame</b>

Главный объект Pandas.

DataFrame — это таблица.

Пример:

<pre><code class="language-python">import pandas as pd

data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Возраст": [20, 25, 30]
}

df = pd.DataFrame(data)

print(df)</code></pre>

Результат:

<pre><code>    Имя  Возраст
0  Анна       20
1  Иван       25
2  Олег       30</code></pre>

━━━━━━━━━━━

DataFrame похож на Excel-таблицу.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Создание DataFrame</b>

Из словаря:

<pre><code class="language-python">data = {
    "Город": ["Москва", "СПб", "Казань"],
    "Население": [13000000, 5600000, 1300000]
}

df = pd.DataFrame(data)</code></pre>

━━━━━━━━━━━

Из списка словарей:

<pre><code class="language-python">data = [
    {"name": "Анна", "age": 20},
    {"name": "Иван", "age": 25}
]

df = pd.DataFrame(data)</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Просмотр данных</b>

Первые строки таблицы:

<pre><code class="language-python">df.head()</code></pre>

По умолчанию показывает первые 5 строк.

━━━━━━━━━━━

Первые 2 строки:

<pre><code class="language-python">df.head(2)</code></pre>

━━━━━━━━━━━

Последние строки:

<pre><code class="language-python">df.tail()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Информация о таблице</b>

Получить информацию:

<pre><code class="language-python">df.info()</code></pre>

Пример вывода:

<pre><code>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 100 entries
Data columns: 3 columns</code></pre>

Показывает:

• количество строк

• количество столбцов

• типы данных

• пропущенные значения

━━━━━━━━━━━
<b>ЧАСТЬ 8. Размер таблицы</b>

Получить размеры:

<pre><code class="language-python">df.shape</code></pre>

Результат:

<pre><code>(100, 5)</code></pre>

Это означает:

• 100 строк

• 5 столбцов

━━━━━━━━━━━
<b>ЧАСТЬ 9. Получение столбца</b>

Получить один столбец:

<pre><code class="language-python">df["Возраст"]</code></pre>

Результат:

<pre><code>0    20
1    25
2    30</code></pre>

Получается объект Series.

━━━━━━━━━━━

Можно так:

<pre><code class="language-python">df.Возраст</code></pre>

Но рекомендуется использовать квадратные скобки.

━━━━━━━━━━━
<b>ЧАСТЬ 10. Несколько столбцов</b>

Пример:

<pre><code class="language-python">df[["Имя", "Возраст"]]</code></pre>

Результат:

Таблица только из двух столбцов.

━━━━━━━━━━━
<b>ЧАСТЬ 11. Получение строки</b>

По индексу:

<pre><code class="language-python">df.iloc[0]</code></pre>

Результат:

Первая строка таблицы.

━━━━━━━━━━━

Вторая строка:

<pre><code class="language-python">df.iloc[1]</code></pre>

━━━━━━━━━━━

Срез:

<pre><code class="language-python">df.iloc[0:3]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Фильтрация данных</b>

Одна из самых мощных возможностей Pandas.

Пример:

<pre><code class="language-python">df[df["Возраст"] > 20]</code></pre>

Результат:

Все люди старше 20 лет.

━━━━━━━━━━━

Можно использовать разные условия.

Меньше:

<pre><code class="language-python">df[df["Возраст"] < 30]</code></pre>

━━━━━━━━━━━

Равно:

<pre><code class="language-python">df[df["Возраст"] == 25]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 13. Несколько условий</b>

Оператор И:

<pre><code class="language-python">df[
    (df["Возраст"] > 20)
    &
    (df["Возраст"] < 30)
]</code></pre>

━━━━━━━━━━━

Оператор ИЛИ:

<pre><code class="language-python">df[
    (df["Возраст"] < 20)
    |
    (df["Возраст"] > 30)
]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 14. Статистика</b>

Среднее значение:

<pre><code class="language-python">df["Возраст"].mean()</code></pre>

━━━━━━━━━━━

Максимум:

<pre><code class="language-python">df["Возраст"].max()</code></pre>

━━━━━━━━━━━

Минимум:

<pre><code class="language-python">df["Возраст"].min()</code></pre>

━━━━━━━━━━━

Сумма:

<pre><code class="language-python">df["Возраст"].sum()</code></pre>

━━━━━━━━━━━

Количество:

<pre><code class="language-python">df["Возраст"].count()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 15. Описание данных</b>

Полезная функция:

<pre><code class="language-python">df.describe()</code></pre>

Она автоматически считает:
• среднее
• минимум
• максимум
• медиану
• квартиль
• стандартное отклонение

━━━━━━━━━━━

Это одна из самых популярных команд в аналитике.

━━━━━━━━━━━
<b>ЧАСТЬ 16. Чтение CSV-файлов</b>

Главная причина популярности Pandas.

Файл:

<pre><code>users.csv</code></pre>

Загрузка:

<pre><code class="language-python">df = pd.read_csv("users.csv")</code></pre>

После этого таблица доступна в DataFrame.

━━━━━━━━━━━
<b>ЧАСТЬ 17. Сохранение CSV</b>

Сохранить таблицу:

<pre><code class="language-python">df.to_csv(
    "result.csv",
    index=False
)</code></pre>

Будет создан новый CSV-файл.

━━━━━━━━━━━
<b>ЧАСТЬ 18. Работа с пропущенными значениями</b>

Проверить пропуски:

<pre><code class="language-python">df.isnull()</code></pre>

━━━━━━━━━━━

Посчитать:

<pre><code class="language-python">df.isnull().sum()</code></pre>

━━━━━━━━━━━

Удалить пропуски:

<pre><code class="language-python">df.dropna()</code></pre>

━━━━━━━━━━━

Заменить пропуски:

<pre><code class="language-python">df.fillna(0)</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 19. Где используется Pandas</b>

📊 Аналитика данных

📈 Бизнес-отчёты

🤖 Машинное обучение

💰 Финансовая аналитика

📉 Обработка больших CSV-файлов

📋 Автоматизация отчётов

🧠 Data Science

━━━━━━━━━━━
<b>ЧАСТЬ 20. Типичные ошибки новичков</b>

<b>❌ Забывают импортировать библиотеку</b>

<pre><code class="language-python">df = pd.DataFrame(...)</code></pre>

Ошибка:

<pre><code>NameError</code></pre>

Нужно:

<pre><code class="language-python">import pandas as pd</code></pre>

━━━━━━━━━━━

<b>❌ Путают Series и DataFrame</b>

<pre><code class="language-python">df["Возраст"]</code></pre>

возвращает Series.

А не таблицу.

━━━━━━━━━━━

<b>❌ Используют обычный and вместо &</b>

Неправильно:

<pre><code class="language-python">df[
    (df["Возраст"] > 20)
    and
    (df["Возраст"] < 30)
]</code></pre>

Правильно:

<pre><code class="language-python">df[
    (df["Возраст"] > 20)
    &
    (df["Возраст"] < 30)
]</code></pre>

━━━━━━━━━━━

<b>❌ Забывают скобки в условиях</b>

Неправильно:

<pre><code class="language-python">df[df["Возраст"] > 20 & df["Возраст"] < 30]</code></pre>

Правильно:

<pre><code class="language-python">df[
    (df["Возраст"] > 20)
    &
    (df["Возраст"] < 30)
]</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• Pandas — главная библиотека для работы с таблицами
• основной объект — DataFrame
• Series представляет один столбец данных
• DataFrame похож на Excel-таблицу
• head() показывает первые строки
• shape показывает размеры таблицы
• iloc позволяет получать строки по индексу
• фильтрация выполняется через условия
• read_csv() читает CSV-файлы
• to_csv() сохраняет данные
• describe() быстро показывает статистику
• Pandas является стандартом в Data Science и аналитике данных