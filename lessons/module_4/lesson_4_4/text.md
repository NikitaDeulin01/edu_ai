<b>🧩 Урок 4.4. Область видимости переменных: Local, Global, Built-in и nonlocal</b>

<i>В прошлом уроке мы познакомились с локальными и глобальными переменными. Теперь разберёмся глубже: как Python ищет переменные, что такое правило LEGB, когда нужен global и зачем существует nonlocal.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое область видимости</b>

Область видимости определяет:

<b>откуда можно обратиться к переменной.</b>

Например:

<pre><code class="language-python">name = "Алекс"

print(name)</code></pre>

Переменная доступна в программе.

Но если создать её внутри функции:

<pre><code class="language-python">def hello():
    name = "Алекс"</code></pre>

использовать её получится только внутри этой функции.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Как Python ищет переменные</b>

Когда Python встречает имя переменной:

<pre><code class="language-python">print(name)</code></pre>

он начинает поиск.

Поиск идёт по правилу:

<pre><code>LEGB</code></pre>

Расшифровка:

<table>
<tr>
<td><b>Буква</b></td>
<td><b>Область</b></td>
</tr>

<tr>
<td>L</td>
<td>Local</td>
</tr>

<tr>
<td>E</td>
<td>Enclosing</td>
</tr>

<tr>
<td>G</td>
<td>Global</td>
</tr>

<tr>
<td>B</td>
<td>Built-in</td>
</tr>
</table>

Python ищет переменную именно в этом порядке.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Local (локальная область)</b>

Локальная область — это переменные внутри функции.

Пример:

<pre><code class="language-python">name = "Глобальная"

def test():
    name = "Локальная"
    print(name)

test()</code></pre>

Результат:

<pre><code>Локальная</code></pre>

Почему?

Потому что Python сначала ищет переменную в Local.

И находит её сразу.

━━━━━━━━━━━

После завершения функции локальные переменные исчезают.

Пример:

<pre><code class="language-python">def test():
    x = 10

test()

print(x)</code></pre>

Ошибка:

<pre><code>NameError</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Global (глобальная область)</b>

Глобальная область — это переменные, созданные вне функций.

Пример:

<pre><code class="language-python">name = "Алекс"

def hello():
    print(name)

hello()</code></pre>

Результат:

<pre><code>Алекс</code></pre>

Функция может читать глобальные переменные.

━━━━━━━━━━━

Но есть важный нюанс.

Посмотрите на код:

<pre><code class="language-python">count = 0

def increase():
    count = count + 1

increase()</code></pre>

Ошибка:

<pre><code>UnboundLocalError</code></pre>

Python решил, что count внутри функции — новая локальная переменная.

Но её значение ещё не существует.

━━━━━━━━━━━
<b>Оператор global</b>

Чтобы изменить глобальную переменную, используют:

<pre><code class="language-python">global</code></pre>

Пример:

<pre><code class="language-python">count = 0

def increase():
    global count
    count += 1

increase()

print(count)</code></pre>

Результат:

<pre><code>1</code></pre>

Теперь Python понимает, что нужно работать с глобальной переменной.

━━━━━━━━━━━
<b>Когда использовать global</b>

Можно использовать.

Но в реальных проектах стараются делать это редко.

Причина проста:

Глобальные переменные делают программу менее предсказуемой.

Лучше передавать данные через параметры функций.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Built-in (встроенная область)</b>

Некоторые функции существуют ещё до запуска вашей программы.

Например:

<pre><code class="language-python">print()
len()
sum()
input()</code></pre>

Где они объявлены?

Не в вашем коде.

Они встроены в Python.

Это называется Built-in область видимости.

━━━━━━━━━━━

Пример:

<pre><code class="language-python">text = "Python"

print(len(text))</code></pre>

Результат:

<pre><code>6</code></pre>

Функция:

<pre><code class="language-python">len()</code></pre>

нашлась именно во встроенной области.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Enclosing (внешняя функция)</b>

Это область между Local и Global.

Появляется только при вложенных функциях.

Пример:

<pre><code class="language-python">def outer():
    message = "Привет"

    def inner():
        print(message)

    inner()

outer()</code></pre>

Результат:

<pre><code>Привет</code></pre>

Переменная:

<pre><code class="language-python">message</code></pre>

не является локальной для inner().

Но и не является глобальной.

Она находится во внешней функции.

Это и есть Enclosing.

━━━━━━━━━━━
<b>ЧАСТЬ 7. Оператор nonlocal</b>

Иногда нужно изменить переменную внешней функции.

Для этого существует:

<pre><code class="language-python">nonlocal</code></pre>

Пример:

<pre><code class="language-python">def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()

outer()</code></pre>

Результат:

<pre><code>1</code></pre>

Без nonlocal возникла бы ошибка.

━━━━━━━━━━━

Ещё пример:

<pre><code class="language-python">def outer():
    text = "Python"

    def inner():
        nonlocal text
        text = "AI"

    inner()

    print(text)

outer()</code></pre>

Результат:

<pre><code>AI</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Полное правило LEGB</b>

Посмотрим на пример.

<pre><code class="language-python">name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()</code></pre>

Результат:

<pre><code>Local</code></pre>

Python нашёл имя на первом уровне поиска.

До остальных уровней даже не дошёл.

━━━━━━━━━━━

Уберём локальную переменную:

<pre><code class="language-python">name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        print(name)

    inner()

outer()</code></pre>

Результат:

<pre><code>Enclosing</code></pre>

Теперь поиск дошёл до E.

━━━━━━━━━━━

Если убрать и её:

<pre><code class="language-python">name = "Global"

def test():
    print(name)

test()</code></pre>

Результат:

<pre><code>Global</code></pre>

Теперь используется G.

━━━━━━━━━━━

Если переменной нет вообще:

<pre><code class="language-python">print(len("Python"))</code></pre>

Python найдёт:

<pre><code class="language-python">len()</code></pre>

в Built-in области.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Частые ошибки новичков</b>

<b>❌ Использование локальной переменной вне функции</b>

<pre><code class="language-python">def test():
    x = 10

print(x)</code></pre>

Ошибка:

<pre><code>NameError</code></pre>

━━━━━━━━━━━

<b>❌ Злоупотребление global</b>

<pre><code class="language-python">global score
global money
global users</code></pre>

Такой код быстро становится сложным.

━━━━━━━━━━━

<b>❌ Путаница между global и nonlocal</b>

<pre><code class="language-python">global</code></pre>

работает с глобальной областью.

<pre><code class="language-python">nonlocal</code></pre>

работает с внешней функцией.

Это разные вещи.

━━━━━━━━━━━

<b>❌ Переопределение встроенных функций</b>

Плохой пример:

<pre><code class="language-python">len = 100

print(len("Python"))</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

Потому что вы затёрли встроенную функцию.

━━━━━━━━━━━
<b>ЧАСТЬ 10. Нужно ли часто использовать nonlocal?</b>

Нет.

В реальных проектах:
• local используется постоянно
• global используется редко
• built-in используется постоянно
• nonlocal встречается довольно редко
