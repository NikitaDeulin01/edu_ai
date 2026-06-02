<b>📈 Урок 7.3. Введение в Matplotlib</b>

<i>После того как данные собраны и обработаны, их часто нужно показать человеку в удобном виде. Таблицы подходят не всегда. Намного проще увидеть закономерность на графике. Для построения графиков в Python чаще всего используют библиотеку Matplotlib.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое Matplotlib</b>

<b>Matplotlib</b> — это библиотека для визуализации данных.

Она позволяет строить:

• линейные графики

• столбчатые диаграммы

• круговые диаграммы

• гистограммы

• точечные графики

• графики функций

━━━━━━━━━━━
Matplotlib используется вместе с:
• NumPy
• Pandas
• Jupyter Notebook
• Data Science
• Machine Learning

━━━━━━━━━━━
<b>ЧАСТЬ 2. Установка библиотеки</b>

Установка:

<pre><code class="language-bash">pip install matplotlib</code></pre>

Импорт:

<pre><code class="language-python">import matplotlib.pyplot as plt</code></pre>

Сокращение <code>plt</code> используется почти во всех проектах.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Первый график</b>

Пример:

<pre><code class="language-python">import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 7, 20]

plt.plot(x, y)

plt.show()</code></pre>

После запуска откроется окно с графиком.

━━━━━━━━━━━

Что здесь происходит:

<pre><code class="language-python">plt.plot(x, y)</code></pre>

рисует график.

<pre><code class="language-python">plt.show()</code></pre>

отображает его на экране.

━━━━━━━━━━━
<b>ЧАСТЬ 4. Как устроен линейный график</b>

Координаты:

<pre><code class="language-python">x = [1, 2, 3]
y = [5, 10, 15]</code></pre>

Создают точки:

<pre><code>(1, 5)
(2, 10)
(3, 15)</code></pre>

Matplotlib соединяет их линиями.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Заголовок графика</b>

Можно добавить название.

<pre><code class="language-python">plt.title("Продажи по месяцам")</code></pre>

Полный пример:

<pre><code class="language-python">plt.plot([1, 2, 3], [10, 20, 30])

plt.title("Продажи")

plt.show()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Подписи осей</b>

Ось X:

<pre><code class="language-python">plt.xlabel("Месяц")</code></pre>

Ось Y:

<pre><code class="language-python">plt.ylabel("Продажи")</code></pre>

Пример:

<pre><code class="language-python">plt.plot([1, 2, 3], [10, 20, 30])

plt.xlabel("Месяц")
plt.ylabel("Доход")

plt.show()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Цвет линии</b>

Можно изменить цвет.

Красная линия:

<pre><code class="language-python">plt.plot(x, y, color="red")</code></pre>

Синяя:

<pre><code class="language-python">plt.plot(x, y, color="blue")</code></pre>

Зелёная:

<pre><code class="language-python">plt.plot(x, y, color="green")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Тип линии</b>

Сплошная:

<pre><code class="language-python">plt.plot(x, y, linestyle="-")</code></pre>

Пунктир:

<pre><code class="language-python">plt.plot(x, y, linestyle="--")</code></pre>

Точки:

<pre><code class="language-python">plt.plot(x, y, linestyle=":")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Маркеры точек</b>

Показывают точки на графике.

Пример:

<pre><code class="language-python">plt.plot(
    x,
    y,
    marker="o"
)</code></pre>

Результат:

Каждая точка будет отмечена кружком.

━━━━━━━━━━━
<b>ЧАСТЬ 10. Столбчатая диаграмма</b>

Используется для сравнения значений.

Пример:

<pre><code class="language-python">names = ["Анна", "Иван", "Олег"]
scores = [80, 95, 70]

plt.bar(names, scores)

plt.show()</code></pre>

Результат:

Появится столбчатая диаграмма.

━━━━━━━━━━━
<b>ЧАСТЬ 11. Круговая диаграмма</b>

Показывает доли.

Пример:

<pre><code class="language-python">values = [40, 30, 20, 10]

plt.pie(values)

plt.show()</code></pre>

━━━━━━━━━━━

С подписями:

<pre><code class="language-python">values = [40, 30, 20, 10]

labels = [
    "Python",
    "Java",
    "C++",
    "Go"
]

plt.pie(
    values,
    labels=labels
)

plt.show()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Точечный график (Scatter Plot)</b>

Используется для анализа зависимостей.

Пример:

<pre><code class="language-python">x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y)

plt.show()</code></pre>

Каждая точка отображается отдельно.

━━━━━━━━━━━
<b>ЧАСТЬ 13. Гистограмма</b>

Используется для анализа распределения данных.

Пример:

<pre><code class="language-python">numbers = [
    10, 11, 12, 12,
    15, 16, 17, 18,
    20, 21, 25
]

plt.hist(numbers)

plt.show()</code></pre>

Гистограмма покажет, какие значения встречаются чаще.

━━━━━━━━━━━
<b>ЧАСТЬ 14. Несколько графиков одновременно</b>

Можно построить несколько линий.

<pre><code class="language-python">x = [1, 2, 3]

sales = [10, 20, 30]
profit = [5, 12, 18]

plt.plot(x, sales)
plt.plot(x, profit)

plt.show()</code></pre>

На одном графике появятся две линии.

━━━━━━━━━━━
<b>ЧАСТЬ 15. Легенда</b>

Чтобы понять, какая линия что означает:

<pre><code class="language-python">plt.plot(
    x,
    sales,
    label="Продажи"
)

plt.plot(
    x,
    profit,
    label="Прибыль"
)

plt.legend()

plt.show()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 16. Сетка</b>

Для удобства анализа.

<pre><code class="language-python">plt.grid(True)</code></pre>

Пример:

<pre><code class="language-python">plt.plot(x, y)

plt.grid(True)

plt.show()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 17. Построение функции</b>

Matplotlib часто используют вместе с NumPy.

Пример:

<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)

y = x ** 2

plt.plot(x, y)

plt.show()</code></pre>

Будет построен график функции:

<pre><code>y = x²</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 18. Pandas + Matplotlib</b>

Часто данные берут из DataFrame.

Пример:

<pre><code class="language-python">import pandas as pd

data = {
    "month": [1, 2, 3],
    "sales": [100, 150, 200]
}

df = pd.DataFrame(data)

plt.plot(
    df["month"],
    df["sales"]
)

plt.show()</code></pre>

Это один из самых распространённых сценариев в аналитике.

━━━━━━━━━━━
<b>ЧАСТЬ 19. Где используется Matplotlib</b>

📈 Аналитика данных

📊 Отчёты

🤖 Машинное обучение

🧠 Data Science

📉 Финансовые графики

🔬 Научные исследования

📋 Дашборды

━━━━━━━━━━━
<b>ЧАСТЬ 20. Типичные ошибки новичков</b>

<b>❌ Забывают вызвать show()</b>

<pre><code class="language-python">plt.plot(x, y)</code></pre>

График может не появиться.

Нужно:

<pre><code class="language-python">plt.show()</code></pre>

━━━━━━━━━━━

<b>❌ Разная длина x и y</b>

Неправильно:

<pre><code class="language-python">x = [1, 2, 3]
y = [10, 20]</code></pre>

Будет ошибка.

Количество элементов должно совпадать.

━━━━━━━━━━━

<b>❌ Путают bar() и plot()</b>

<pre><code class="language-python">plot()</code></pre>

рисует линии.

<pre><code class="language-python">bar()</code></pre>

рисует столбцы.

━━━━━━━━━━━

<b>❌ Не импортируют pyplot</b>

Ошибка:

<pre><code>NameError: plt is not defined</code></pre>

Нужно:

<pre><code class="language-python">import matplotlib.pyplot as plt</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• Matplotlib — главная библиотека визуализации данных в Python
• pyplot обычно импортируют как plt
• plot() строит линейные графики
• bar() строит столбчатые диаграммы
• pie() строит круговые диаграммы
• scatter() строит точечные графики
• hist() строит гистограммы
• title() добавляет заголовок
• xlabel() и ylabel() подписывают оси
• legend() показывает легенду
• show() отображает график
• Matplotlib часто используется вместе с NumPy и Pandas