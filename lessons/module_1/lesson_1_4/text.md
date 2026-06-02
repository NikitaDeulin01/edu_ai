<b>📦 Урок 2. Переменные и типы данных</b>

━━━━━━━━━━

<b>👋 Зачем нужны переменные?</b>

Допустим, мы пишем программу-приветствие. Имя пользователя заранее неизвестно — оно появится только при запуске. В коде нужно ссылаться на это будущее имя. Для этого существуют <b>переменные</b>.

<pre><code class="language-python">name = "Иван"
print("Привет, " + name + "!")</code></pre>

Здесь <code>name</code> — «подпись», под которой Python запоминает, где в памяти лежит строка <code>"Иван"</code>. Когда встречается <code>name</code>, подставляется значение.

<i>📷 Схема «переменная → объект в памяти» — положите в images/ (например, 01_variable_memory.png).</i>

━━━━━━━━━━

<b>🔍 Что такое переменная?</b>

<b>Переменная в Python</b> — имя, привязанное к объекту в памяти. Тип Python определяет сам; привязку можно менять в любой момент.

<b>Три удобства:</b>
• не нужно объявлять переменную заранее — она появляется при первом присваивании;
• не нужно указывать тип — Python смотрит, что справа;
• можно перепривязать имя к другому значению.

━━━━━━━━━━

<b>✏️ Создание и использование</b>

Слева — имя, справа — значение (оператор <code>=</code>):

<pre><code class="language-python">name = "Иван"          # str
age = 25               # int
height = 1.85          # float
is_student = True      # bool
courses = ["Python", "SQL", "JavaScript"]  # list</code></pre>

<b>Примеры в интерактивной консоли:</b>

<pre><code class="language-python">&gt;&gt;&gt; name = "Иван"
&gt;&gt;&gt; print("Привет, " + name + "!")
Привет, Иван!

&gt;&gt;&gt; age = 25
&gt;&gt;&gt; next_year_age = age + 1
&gt;&gt;&gt; print(f"В следующем году тебе будет {next_year_age} лет")
В следующем году тебе будет 26 лет</code></pre>

━━━━━━━━━━

<b>📦 Множественное присваивание</b>

<b>Распаковка</b> — справа коллекция, слева несколько имён:

<pre><code class="language-python">&gt;&gt;&gt; coordinates = (10, 20, 30)
&gt;&gt;&gt; x, y, z = coordinates
&gt;&gt;&gt; print(f"x={x}, y={y}, z={z}")
x=10, y=20, z=30</code></pre>

<b>Обмен значений</b> без временной переменной:

<pre><code class="language-python">&gt;&gt;&gt; a = 5
&gt;&gt;&gt; b = 10
&gt;&gt;&gt; a, b = b, a
&gt;&gt;&gt; print(f"a = {a}, b = {b}")
a = 10, b = 5</code></pre>

Справа собирается кортеж <code>(10, 5)</code>, слева он распаковывается.

<b>Цепочка присваивания</b> (одно значение нескольким именам):

<pre><code class="language-python">x = y = z = 0</code></pre>

В реальном коде редко. С изменяемыми объектами <code>a = b = []</code> даст <b>один и тот же список</b> — обычно это не то, что нужно.

━━━━━━━━━━

<b>🔄 Динамическая типизация</b>

Тип определяется при выполнении и может меняться:

<pre><code class="language-python">&gt;&gt;&gt; x = 10
&gt;&gt;&gt; print(f"x = {x}, тип: {type(x)}")
x = 10, тип: &lt;class 'int'&gt;

&gt;&gt;&gt; x = "десять"
&gt;&gt;&gt; print(f"x = {x}, тип: {type(x)}")
x = десять, тип: &lt;class 'str'&gt;

&gt;&gt;&gt; x = [1, 2, 3]
&gt;&gt;&gt; print(f"x = {x}, тип: {type(x)}")
x = [1, 2, 3], тип: &lt;class 'list'&gt;</code></pre>

Функция <code>type()</code> показывает текущий тип:

<pre><code class="language-python">&gt;&gt;&gt; name = "Иван"
&gt;&gt;&gt; age = 25
&gt;&gt;&gt; print(f"{name}: {type(name)}")
Иван: &lt;class 'str'&gt;
&gt;&gt;&gt; print(f"{age}: {type(age)}")
25: &lt;class 'int'&gt;</code></pre>

━━━━━━━━━━

<b>🏷 Именование переменных</b>

Хорошие имена делают код понятным.

<b>Правила:</b>
• буквы, цифры, <code>_</code> (a–z, A–Z, 0–9, _);
• начало — с буквы или <code>_</code>;
• нельзя зарезервированные слова (<code>if</code>, <code>for</code>, <code>class</code>…).

<pre><code class="language-python"># ✅ Допустимо
name = "Иван"
age_in_years = 25
_private_variable = "скрытое"

# ❌ Нельзя
# 2name = "..."
# my-name = "..."
# class = "..."</code></pre>

━━━━━━━━━━

<b>📐 PEP 8 — лучшие практики</b>

<b>Описательные имена:</b>
<pre><code class="language-python">user_age = 25   # ✅
a = 25          # ❌ через месяц непонятно</code></pre>

<b>snake_case</b> (слова через <code>_</code>):
<pre><code class="language-python">first_name = "Иван"   # ✅
firstName = "Иван"    # не в стиле Python</code></pre>

<b>Булевы переменные</b> — префиксы <code>is_</code>, <code>has_</code>:
<pre><code class="language-python">is_adult = True
has_permission = False</code></pre>

<b>Константы</b> — ВЕРХНИЙ_РЕГИСТР:
<pre><code class="language-python">MAX_ATTEMPTS = 3
PI = 3.14159</code></pre>

В Python константы не «запираются» — это соглашение команды.

<b>Избегайте слишком коротких имён:</b>
<pre><code class="language-python">user_name = "Иван"       # ✅
welcome_message = "..."  # ✅
n = "Иван"               # ❌</code></pre>

Код читают чаще, чем пишут — лишние символы в имени окупаются.

━━━━━━━━━━

<b>🔤 Регистрозависимость</b>

<code>name</code>, <code>Name</code> и <code>NAME</code> — <b>три разные переменные</b>:

<pre><code class="language-python">&gt;&gt;&gt; name = "Иван"
&gt;&gt;&gt; Name = "Пётр"
&gt;&gt;&gt; NAME = "Алексей"
&gt;&gt;&gt; print(name, Name, NAME)
Иван Пётр Алексей</code></pre>

━━━━━━━━━━

<b>✅ Итог урока</b>

• переменная = имя + ссылка на объект;
• присваивание через <code>=</code>, тип не объявляем;
• распаковка и обмен <code>a, b = b, a</code>;
• имена по PEP 8: snake_case, is_/has_, КОНСТАНТЫ в верхнем регистре.
