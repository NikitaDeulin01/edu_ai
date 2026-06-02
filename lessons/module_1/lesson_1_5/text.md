<b>🔢 Урок 3. Базовые типы данных</b>

<i>Один урок: числа, строки, логика. Читайте по частям — бот разобьёт текст автоматически. Картинки (схемы, индексы строк) — в images/ в конце.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Числовые типы</b>

<b>Основные типы:</b>
• <code>int</code> — целые числа
• <code>float</code> — с дробной частью
• <code>complex</code> — комплексные (в быту почти не нужны)

<b>Целые числа (int)</b>

<pre><code class="language-python">positive = 42
negative = -73
zero = 0
million = 1_000_000  # удобно читать большие числа</code></pre>

В Python целые числа <b>неограниченной точности</b> (пока хватает памяти).

<b>Числа с плавающей точкой (float)</b>

<pre><code class="language-python">price = 19.99
pi_approx = 3.14159</code></pre>

<b>⚠️ Погрешность float:</b>

<pre><code class="language-python">&gt;&gt;&gt; print(0.1 + 0.2)
0.30000000000000004
&gt;&gt;&gt; print(0.1 + 0.2 == 0.3)
False</code></pre>

Для денег и точных расчётов — модуль <code>decimal</code>. Сравнивать дроби лучше так:

<pre><code class="language-python">import math
print(math.isclose(0.1 + 0.2, 0.3))  # True</code></pre>

<b>Арифметика</b>

<pre><code class="language-python">a, b = 10, 3
a + b   # 13
a - b   # 7
a * b   # 30
a / b   # 3.333...  всегда float
a // b  # 3         целочисленное деление
a % b   # 1         остаток
a ** b  # 1000      степень</code></pre>

<b>Смешанные типы:</b> int + float → всегда <code>float</code>.

<b>Округление</b>

<pre><code class="language-python">round(3.14159)      # 3
round(3.14159, 2)   # 3.14

import math
math.floor(3.99)    # 3
math.ceil(3.01)     # 4
math.trunc(3.99)    # 3</code></pre>

<b>Банковское округление:</b> при «ровно посередине» round идёт к ближайшему чётному:

<pre><code class="language-python">&gt;&gt;&gt; round(0.5)   # 0
&gt;&gt;&gt; round(1.5)   # 2
&gt;&gt;&gt; round(2.5)   # 2</code></pre>

<b>Модуль math</b> — <code>sqrt</code>, <code>pi</code>, <code>e</code>, тригонометрия и др.

<b>Встроенные функции:</b> <code>abs</code>, <code>max</code>, <code>min</code>, <code>sum</code>, <code>int()</code>, <code>float()</code>.

<i>📷 Картинка по числам — images/01_numbers.png (по желанию).</i>

━━━━━━━━━━━
<b>ЧАСТЬ 2. Строки (str)</b>

<b>Строка</b> — последовательность символов для текста.

<b>Создание</b> — одинарные, двойные или тройные кавычки:

<pre><code class="language-python">&gt;&gt;&gt; single = 'Привет, мир!'
&gt;&gt;&gt; double = "Hello, world"
&gt;&gt;&gt; multi = """Рецепт кофе:
... 1. Вскипятить воду
... 2. Залить кофе
... 3. Подождать 4 минуты"""</code></pre>

• <code>'</code> и <code>"</code> — одинаково
• если внутри есть <code>'</code> — оборачивайте в <code>"</code>, и наоборот
• <code>"""</code> — для многострочного текста

<b>Экранирование</b> — символ <code>\</code>:

<pre><code class="language-python">quote = "Он сказал: \"Привет!\""
path = "C:\\Program Files\\Python"
newline = "Первая строка.\nВторая строка."
tab = "Имя:\tИван"</code></pre>

Частые последовательности: <code>\n</code> <code>\t</code> <code>\\</code> <code>\'</code> <code>\"</code>

<b>Raw-строки</b> (префикс <code>r</code>) — обратный слеш «как есть»:

<pre><code class="language-python">raw_path = r"C:\Users\Username\Documents"</code></pre>

Удобно для путей Windows и регулярных выражений.

<b>Неизменяемость (immutable)</b>

Строку нельзя менять по индексу:

<pre><code class="language-python">language = "Python"
# language[0] = "J"  # TypeError

language = "J" + "ython"  # новая строка</code></pre>

<b>Операции</b>

<pre><code class="language-python">first_name + " " + last_name   # конкатенация
"=" * 20                       # повторение
len("Python")                  # 6</code></pre>

<b>Индексы и срезы</b>

Индексация с 0; отрицательные — с конца:

<pre><code class="language-python">word = "Python"
word[0]    # 'P'
word[-1]   # 'n'

message = "Python Programming"
message[0:6]    # 'Python'
message[7:]     # 'Programming'
message[::2]    # каждый второй символ
message[::-1]   # наоборот</code></pre>

<i>📷 Схема индексов строки — images/02_string_indexes.png</i>

<b>Полезные методы</b>

<pre><code class="language-python">text.upper() / text.lower() / text.title() / text.capitalize()
text.find("подстрока")   text.count("о")
text.startswith("Py")    text.endswith("!")
"подстрока" in text
text.replace("старое", "новое")
text.split()             text.split(",")
" ".join(words)
text.strip()  text.lstrip()  text.rstrip()</code></pre>

<b>Цепочки методов</b>

<pre><code class="language-python">normalized = raw_input.strip().lower()</code></pre>

Каждый метод возвращает <b>новую</b> строку — можно вызывать подряд.

<b>f-строки</b> (современный способ форматирования):

<pre><code class="language-python">name, age = "Анна", 25
greeting = f"Привет, {name}, тебе {age} лет."

price, quantity = 19.99, 3
total = f"Итого: {price * quantity:.2f} руб."</code></pre>

Старые способы <code>.format()</code> и <code>%</code> в новом коде почти не используют.

<i>📷 Иллюстрации к строкам — images/03_strings.png (по желанию).</i>

━━━━━━━━━━━
<b>ЧАСТЬ 3. Логический тип (bool)</b>

Тип <code>bool</code> — только <code>True</code> и <code>False</code>. Пишутся <b>с большой буквы</b>.

<pre><code class="language-python">is_raining = True
print(type(is_raining))  # &lt;class 'bool'&gt;</code></pre>

<b>Логические операторы</b>

• <code>and</code> — истина, если оба True
• <code>or</code> — истина, если хотя бы один True
• <code>not</code> — инверсия

<pre><code class="language-python">going_to_beach = sunny and warm
will_buy_phone = beautiful or cheap
not have_homework</code></pre>

<b>Сравнения</b> — дают bool:

<pre><code class="language-python">my_age == friend_age
my_age != friend_age
my_age &lt; friend_age
'apple' &lt; 'banana'   # лексикографически</code></pre>

<b>== vs is</b>

• <code>==</code> — одинаковое <b>содержимое</b>
• <code>is</code> — один и тот же <b>объект в памяти</b>

<pre><code class="language-python">my_scores == friend_scores   # True (одинаковые списки)
my_scores is friend_scores   # False (разные объекты)
my_scores is same_list       # True</code></pre>

<b>Правило:</b> почти всегда нужен <code>==</code>. <code>is</code> — для <code>None</code>, иногда <code>True</code>/<code>False</code>.

<b>Приоритет:</b> <code>not</code> → <code>and</code> → <code>or</code>. Сомневаетесь — ставьте скобки.

<pre><code class="language-python">can_travel = has_ticket and (has_passport or has_visa)</code></pre>

<b>Истинность значений</b>

<pre><code class="language-python">bool(100)    # True
bool(0)      # False
bool("Hi")   # True
bool("")     # False</code></pre>

<b>Ложными (False)</b> считаются:
<code>False</code>, <code>None</code>, <code>0</code>, <code>0.0</code>, пустые <code>""</code> <code>()</code> <code>[]</code> <code>{}</code>

<pre><code class="language-python">money = 0
if money:
    print("Есть деньги")
else:
    print("Кошелёк пуст")  # сработает это

name = "Алекс"
if name:
    print(f"Привет, {name}")</code></pre>

