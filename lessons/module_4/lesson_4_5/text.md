<b>🧩 Урок 4.5. Анонимные функции (lambda)</b>

<i>До этого момента мы создавали функции через def и давали им имена. Но в Python существует ещё один способ создавать функции — с помощью lambda. Такие функции часто используются в обработке данных, сортировках и функциональном программировании.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое анонимная функция</b>

Обычно функция создаётся так:

<pre><code class="language-python">def square(x):
    return x * x</code></pre>

У этой функции есть имя:

<pre><code class="language-python">square</code></pre>

Иногда функция нужна всего один раз.

В таких случаях можно использовать анонимную функцию.

Для этого существует ключевое слово:

<pre><code class="language-python">lambda</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 2. Первая lambda-функция</b>

Обычная функция:

<pre><code class="language-python">def square(x):
    return x * x</code></pre>

То же самое через lambda:

<pre><code class="language-python">square = lambda x: x * x</code></pre>

Использование:

<pre><code class="language-python">print(square(5))</code></pre>

Результат:

<pre><code>25</code></pre>

Обе версии работают одинаково.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Синтаксис lambda</b>

Общий синтаксис:

<pre><code class="language-python">lambda параметры: выражение</code></pre>

После двоеточия указывается выражение, результат которого будет автоматически возвращён.

Примеры:

<pre><code class="language-python">lambda x: x + 1</code></pre>

<pre><code class="language-python">lambda x: x * 2</code></pre>

<pre><code class="language-python">lambda name: f"Привет, {name}"</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Несколько аргументов</b>

Lambda может принимать несколько аргументов.

Пример:

<pre><code class="language-python">multiply = lambda a, b: a * b

print(multiply(3, 4))</code></pre>

Результат:

<pre><code>12</code></pre>

Ещё пример:

<pre><code class="language-python">add = lambda a, b, c: a + b + c

print(add(1, 2, 3))</code></pre>

Результат:

<pre><code>6</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Чем lambda отличается от def</b>

Обычная функция:

<pre><code class="language-python">def add(a, b):
    return a + b</code></pre>

Lambda:

<pre><code class="language-python">lambda a, b: a + b</code></pre>

Главное отличие:

<b>lambda содержит только одно выражение.</b>

Нельзя написать:

<pre><code class="language-python">lambda x:
    print(x)
    return x * 2</code></pre>

Такой код вызовет ошибку.

━━━━━━━━━━━
<b>Ограничения lambda</b>

В lambda нельзя:

• писать несколько строк кода

• использовать return

• создавать циклы

• писать сложную бизнес-логику

Lambda предназначена только для коротких операций.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Lambda и sorted()</b>

Одно из самых частых применений lambda — сортировка.

Предположим, есть список пользователей:

<pre><code class="language-python">users = [
    ("Алекс", 25),
    ("Иван", 18),
    ("Мария", 30)
]</code></pre>

Отсортируем по возрасту:

<pre><code class="language-python">users.sort(key=lambda user: user[1])

print(users)</code></pre>

Результат:

<pre><code>[('Иван', 18),
 ('Алекс', 25),
 ('Мария', 30)]</code></pre>

━━━━━━━━━━━

Отсортируем по имени:

<pre><code class="language-python">users.sort(key=lambda user: user[0])</code></pre>

Теперь сортировка будет происходить по первому элементу кортежа.

━━━━━━━━━━━
<b>ЧАСТЬ 7. Lambda и map()</b>

Функция:

<pre><code class="language-python">map()</code></pre>

применяет действие к каждому элементу последовательности.

Пример:

<pre><code class="language-python">numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))</code></pre>

Результат:

<pre><code>[2, 4, 6, 8]</code></pre>

Каждое число было умножено на два.

━━━━━━━━━━━
<b>ЧАСТЬ 8. Lambda и filter()</b>

Функция:

<pre><code class="language-python">filter()</code></pre>

оставляет только элементы, удовлетворяющие условию.

Пример:

<pre><code class="language-python">numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))</code></pre>

Результат:

<pre><code>[2, 4, 6]</code></pre>

Остались только чётные числа.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Lambda и условные выражения</b>

Внутри lambda можно использовать тернарный оператор.

Пример:

<pre><code class="language-python">check = lambda age: "Взрослый" if age >= 18 else "Ребёнок"

print(check(20))</code></pre>

Результат:

<pre><code>Взрослый</code></pre>

━━━━━━━━━━━

Ещё пример:

<pre><code class="language-python">parity = lambda x: "Чётное" if x % 2 == 0 else "Нечётное"

print(parity(7))</code></pre>

Результат:

<pre><code>Нечётное</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Когда использовать lambda</b>

Хорошие случаи:

✅ короткая функция

✅ функция нужна один раз

✅ работа с sorted()

✅ работа с map()

✅ работа с filter()

━━━━━━━━━━━

Неудачные случаи:

❌ сложные вычисления

❌ много условий

❌ несколько строк логики

❌ большие функции

В таких ситуациях лучше использовать обычный:

<pre><code class="language-python">def</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Частые ошибки новичков</b>

<b>❌ Использование return</b>

Неправильно:

<pre><code class="language-python">lambda x: return x * 2</code></pre>

Ошибка.

Правильно:

<pre><code class="language-python">lambda x: x * 2</code></pre>

━━━━━━━━━━━

<b>❌ Несколько инструкций внутри lambda</b>

Неправильно:

<pre><code class="language-python">lambda x:
    print(x)
    x * 2</code></pre>

Ошибка.

Lambda допускает только одно выражение.

━━━━━━━━━━━

<b>❌ Слишком сложная lambda</b>

Плохо:

<pre><code class="language-python">lambda x, y, z: (x + y) * z if z > 0 else (x - y) / z</code></pre>

Такой код сложно читать.

Лучше написать обычную функцию.

━━━━━━━━━━━

<b>❌ Использование lambda без необходимости</b>

Иногда обычная функция выглядит понятнее:

<pre><code class="language-python">def square(x):
    return x * x</code></pre>

Читается легче, чем длинная lambda-конструкция.