<b>📊 Урок 7.1. Введение в NumPy</b>

<i>До этого момента мы работали со стандартными списками Python. Они отлично подходят для большинства задач, но когда речь идёт о больших объёмах чисел, вычислениях, анализе данных или машинном обучении — используются специальные библиотеки. Самая популярная из них — NumPy.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое NumPy</b>

<b>NumPy</b> (Numerical Python) — это библиотека для работы с массивами и математическими вычислениями.
Она используется в:
• Data Science
• Machine Learning
• Аналитике данных
• Компьютерном зрении
• Научных вычислениях
• Искусственном интеллекте

━━━━━━━━━━━

Практически все современные библиотеки анализа данных построены поверх NumPy.

Например:

• Pandas

• Scikit-Learn

• TensorFlow

• PyTorch

━━━━━━━━━━━
<b>ЧАСТЬ 2. Установка NumPy</b>

Установка через pip:

<pre><code class="language-bash">pip install numpy</code></pre>

Импорт в программу:

<pre><code class="language-python">import numpy as np</code></pre>

Сокращение <code>np</code> используется практически во всех проектах.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Что такое ndarray</b>

Главный объект NumPy называется:

<pre><code class="language-python">ndarray</code></pre>

Это многомерный массив данных.

Создание массива:

<pre><code class="language-python">import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)</code></pre>

Результат:

<pre><code>[1 2 3 4 5]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Отличие списка от массива</b>

Обычный список Python:

<pre><code class="language-python">numbers = [1, 2, 3, 4, 5]</code></pre>

NumPy-массив:

<pre><code class="language-python">numbers = np.array([1, 2, 3, 4, 5])</code></pre>

Внешне похожи.

Но внутри работают совершенно по-разному.

NumPy хранит данные гораздо эффективнее и выполняет вычисления значительно быстрее.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Математика над массивами</b>

В обычном Python:

<pre><code class="language-python">numbers = [1, 2, 3]

numbers * 2</code></pre>

Результат:

<pre><code>[1, 2, 3, 1, 2, 3]</code></pre>

Список просто повторяется.

━━━━━━━━━━━

В NumPy:

<pre><code class="language-python">import numpy as np

numbers = np.array([1, 2, 3])

print(numbers * 2)</code></pre>

Результат:

<pre><code>[2 4 6]</code></pre>

Каждый элемент был умножен на 2.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Арифметические операции</b>

NumPy умеет выполнять операции сразу над всем массивом.

Сложение:

<pre><code class="language-python">arr = np.array([1, 2, 3])

print(arr + 5)</code></pre>

Результат:

<pre><code>[6 7 8]</code></pre>

━━━━━━━━━━━

Вычитание:

<pre><code class="language-python">print(arr - 1)</code></pre>

Результат:

<pre><code>[0 1 2]</code></pre>

━━━━━━━━━━━

Умножение:

<pre><code class="language-python">print(arr * 3)</code></pre>

Результат:

<pre><code>[3 6 9]</code></pre>

━━━━━━━━━━━

Деление:

<pre><code class="language-python">print(arr / 2)</code></pre>

Результат:

<pre><code>[0.5 1.  1.5]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Создание специальных массивов</b>

Массив из нулей:

<pre><code class="language-python">np.zeros(5)</code></pre>

Результат:

<pre><code>[0. 0. 0. 0. 0.]</code></pre>

━━━━━━━━━━━

Массив из единиц:

<pre><code class="language-python">np.ones(5)</code></pre>

Результат:

<pre><code>[1. 1. 1. 1. 1.]</code></pre>

━━━━━━━━━━━

Массив случайных чисел:

<pre><code class="language-python">np.random.rand(5)</code></pre>

Результат:

<pre><code>[0.12 0.83 0.47 0.29 0.91]</code></pre>

Значения будут разными при каждом запуске.

━━━━━━━━━━━
<b>ЧАСТЬ 8. Функция arange()</b>

Аналог range() из Python.

Пример:

<pre><code class="language-python">np.arange(5)</code></pre>

Результат:

<pre><code>[0 1 2 3 4]</code></pre>

━━━━━━━━━━━

Диапазон:

<pre><code class="language-python">np.arange(1, 10)</code></pre>

Результат:

<pre><code>[1 2 3 4 5 6 7 8 9]</code></pre>

━━━━━━━━━━━

С шагом:

<pre><code class="language-python">np.arange(0, 20, 5)</code></pre>

Результат:

<pre><code>[ 0  5 10 15]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Двумерные массивы</b>

NumPy поддерживает таблицы.

Создание:

<pre><code class="language-python">matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])</code></pre>

Вывод:

<pre><code>[[1 2 3]
 [4 5 6]]</code></pre>

Такой массив имеет:

• строки

• столбцы

━━━━━━━━━━━
<b>ЧАСТЬ 10. Размерность массива</b>

Получить форму массива:

<pre><code class="language-python">matrix.shape</code></pre>

Результат:

<pre><code>(2, 3)</code></pre>

Это означает:

• 2 строки

• 3 столбца

━━━━━━━━━━━

Количество измерений:

<pre><code class="language-python">matrix.ndim</code></pre>

Результат:

<pre><code>2</code></pre>

━━━━━━━━━━━

Количество элементов:

<pre><code class="language-python">matrix.size</code></pre>

Результат:

<pre><code>6</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Индексация</b>

Работает почти как в списках.

Первый элемент:

<pre><code class="language-python">arr = np.array([10, 20, 30])

print(arr[0])</code></pre>

Результат:

<pre><code>10</code></pre>

━━━━━━━━━━━

Для матрицы:

<pre><code class="language-python">matrix = np.array([
    [1, 2],
    [3, 4]
])

print(matrix[0][1])</code></pre>

Результат:

<pre><code>2</code></pre>

━━━━━━━━━━━

Более NumPy-стиль:

<pre><code class="language-python">print(matrix[0, 1])</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Срезы (Slicing)</b>

Работают как у строк и списков.

Пример:

<pre><code class="language-python">arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])</code></pre>

Результат:

<pre><code>[20 30 40]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 13. Полезные математические функции</b>

Сумма элементов:

<pre><code class="language-python">arr.sum()</code></pre>

━━━━━━━━━━━

Среднее значение:

<pre><code class="language-python">arr.mean()</code></pre>

━━━━━━━━━━━

Минимум:

<pre><code class="language-python">arr.min()</code></pre>

━━━━━━━━━━━

Максимум:

<pre><code class="language-python">arr.max()</code></pre>

━━━━━━━━━━━

Пример:

<pre><code class="language-python">arr = np.array([10, 20, 30])

print(arr.sum())
print(arr.mean())
print(arr.max())</code></pre>

Результат:

<pre><code>60
20.0
30</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 14. Почему NumPy такой быстрый</b>

Обычные списки Python:

• могут хранить разные типы данных

• более гибкие

• работают медленнее

━━━━━━━━━━━

NumPy:

• хранит данные одного типа

• использует оптимизированный код на C

• работает значительно быстрее

━━━━━━━━━━━

Поэтому массив из миллиона чисел NumPy обрабатывает намного быстрее обычного списка.

━━━━━━━━━━━
<b>ЧАСТЬ 15. Где используется NumPy</b>

NumPy встречается практически везде:

📈 Аналитика данных

🤖 Машинное обучение

🧠 Нейросети

📊 Pandas

📷 Обработка изображений

🎮 Игровая разработка

🔬 Научные вычисления

━━━━━━━━━━━
<b>ЧАСТЬ 16. Типичные ошибки новичков</b>

<b>❌ Забывают импортировать NumPy</b>

<pre><code class="language-python">arr = np.array([1, 2, 3])</code></pre>

Ошибка:

<pre><code>NameError</code></pre>

Нужно:

<pre><code class="language-python">import numpy as np</code></pre>

━━━━━━━━━━━

<b>❌ Путают список и массив</b>

<pre><code class="language-python">[1, 2, 3] * 2</code></pre>

и

<pre><code class="language-python">np.array([1, 2, 3]) * 2</code></pre>

дают разный результат.

━━━━━━━━━━━

<b>❌ Используют NumPy для всего подряд</b>

Если у вас список из 5 элементов — обычный list вполне подходит.

NumPy нужен тогда, когда начинаются вычисления и работа с данными.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• NumPy — главная библиотека для числовых вычислений
• основной объект — ndarray
• массивы NumPy быстрее обычных списков
• операции выполняются сразу над всем массивом
• np.array() создаёт массив
• np.zeros() создаёт массив из нулей
• np.ones() создаёт массив из единиц
• np.arange() создаёт диапазон чисел
• shape показывает размеры массива
• sum(), mean(), min(), max() помогают выполнять вычисления
• NumPy является фундаментом для Data Science и Machine Learning