<b>🧩 Урок 4.2. Аргументы, параметры и return</b>

<i>В прошлом уроке мы научились создавать и вызывать функции. Но пока наши функции выполняли одно и то же действие. В этом уроке вы узнаете, как передавать данные внутрь функции и получать результат обратно.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Зачем нужны параметры</b>

Посмотрим на функцию:

<pre><code class="language-python">def hello():
    print("Привет!")</code></pre>

Она всегда выводит одно и то же сообщение.

А если нужно приветствовать разных людей?

Без параметров пришлось бы создавать много функций:

<pre><code class="language-python">def hello_alex():
    print("Привет, Алекс!")

def hello_ivan():
    print("Привет, Иван!")</code></pre>

Это неудобно.

Гораздо лучше передавать данные внутрь функции.

Для этого существуют параметры.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Что такое параметр</b>

Параметр — это переменная, которая создаётся внутри функции и получает значение при вызове.

Пример:

<pre><code class="language-python">def hello(name):
    print("Привет,", name)</code></pre>

Здесь:

<pre><code class="language-python">name</code></pre>

— параметр функции.

Теперь можно передавать разные значения.

━━━━━━━━━━━
<b>Вызов функции с аргументом</b>

<pre><code class="language-python">def hello(name):
    print("Привет,", name)

hello("Алекс")
hello("Мария")</code></pre>

Результат:

<pre><code>Привет, Алекс
Привет, Мария</code></pre>

Значение, которое передаётся при вызове функции, называется аргументом.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Аргумент и параметр — в чём разница</b>

Новички часто путают эти понятия.

Пример:

<pre><code class="language-python">def hello(name):
    print(name)

hello("Иван")</code></pre>

Параметр:

<pre><code class="language-python">name</code></pre>

Аргумент:

<pre><code class="language-python">"Иван"</code></pre>

Простое правило:

• параметр находится в определении функции

• аргумент передаётся при вызове

━━━━━━━━━━━
<b>ЧАСТЬ 4. Несколько параметров</b>

Функция может принимать несколько значений.

Пример:

<pre><code class="language-python">def introduce(name, age):
    print(name)
    print(age)</code></pre>

Вызов:

<pre><code class="language-python">introduce("Анна", 20)</code></pre>

Результат:

<pre><code>Анна
20</code></pre>

Порядок аргументов важен.

━━━━━━━━━━━
<b>Пример с ошибкой</b>

<pre><code class="language-python">introduce(20, "Анна")</code></pre>

Результат будет неправильным:

<pre><code>20
Анна</code></pre>

Потому что значения передались не тем параметрам.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Использование параметров в вычислениях</b>

Параметры можно использовать как обычные переменные.

Пример:

<pre><code class="language-python">def show_sum(a, b):
    print(a + b)

show_sum(5, 3)</code></pre>

Результат:

<pre><code>8</code></pre>

Во время выполнения:

<pre><code class="language-python">a = 5
b = 3</code></pre>

После этого Python вычисляет сумму.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Возврат результата через return</b>

Обычно функции не просто выводят результат, а возвращают его.

Пример:

<pre><code class="language-python">def sum_numbers(a, b):
    return a + b</code></pre>

Вызов:

<pre><code class="language-python">result = sum_numbers(5, 3)

print(result)</code></pre>

Результат:

<pre><code>8</code></pre>

Функция вернула результат вычисления.

━━━━━━━━━━━
<b>Почему return лучше print</b>

Сравним.

Через print:

<pre><code class="language-python">def sum_numbers(a, b):
    print(a + b)</code></pre>

Через return:

<pre><code class="language-python">def sum_numbers(a, b):
    return a + b</code></pre>

Второй вариант гораздо полезнее.

Мы можем использовать результат дальше:

<pre><code class="language-python">x = sum_numbers(5, 3)

print(x * 2)</code></pre>

Результат:

<pre><code>16</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Несколько return в функции</b>

Функция может содержать несколько вариантов возврата результата.

Пример:

<pre><code class="language-python">def check_age(age):
    if age >= 18:
        return "Совершеннолетний"

    return "Несовершеннолетний"</code></pre>

Вызов:

<pre><code class="language-python">print(check_age(20))</code></pre>

Результат:

<pre><code>Совершеннолетний</code></pre>

Как только выполняется return, функция сразу завершается.

━━━━━━━━━━━
<b>Код после return не выполняется</b>

Пример:

<pre><code class="language-python">def test():
    return 10
    print("Привет")</code></pre>

Строка:

<pre><code class="language-python">print("Привет")</code></pre>

никогда не выполнится.

Потому что функция уже завершилась.

━━━━━━━━━━━
<b>ЧАСТЬ 8. Именованные аргументы</b>

Аргументы можно передавать по имени.

Пример:

<pre><code class="language-python">def introduce(name, age):
    print(name)
    print(age)

introduce(age=20, name="Анна")</code></pre>

Результат:

<pre><code>Анна
20</code></pre>

Теперь порядок аргументов не важен.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Значения по умолчанию</b>

Функция может иметь стандартное значение параметра.

Пример:

<pre><code class="language-python">def hello(name="Друг"):
    print("Привет,", name)</code></pre>

Вызов:

<pre><code class="language-python">hello()</code></pre>

Результат:

<pre><code>Привет, Друг</code></pre>

Можно передать своё значение:

<pre><code class="language-python">hello("Алекс")</code></pre>

Результат:

<pre><code>Привет, Алекс</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Практические примеры</b>

<b>Площадь квадрата</b>

<pre><code class="language-python">def square_area(side):
    return side * side

print(square_area(4))</code></pre>

Результат:

<pre><code>16</code></pre>

━━━━━━━━━━━

<b>Умножение чисел</b>

<pre><code class="language-python">def multiply(a, b):
    return a * b

print(multiply(3, 5))</code></pre>

Результат:

<pre><code>15</code></pre>

━━━━━━━━━━━

<b>Приветствие пользователя</b>

<pre><code class="language-python">def greet(name):
    return f"Привет, {name}!"

print(greet("Олег"))</code></pre>

Результат:

<pre><code>Привет, Олег!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Частые ошибки новичков</b>

<b>❌ Передано слишком мало аргументов</b>

<pre><code class="language-python">def sum_numbers(a, b):
    return a + b

sum_numbers(5)</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

Потому что не хватает второго аргумента.

━━━━━━━━━━━

<b>❌ Передано слишком много аргументов</b>

<pre><code class="language-python">sum_numbers(1, 2, 3)</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

━━━━━━━━━━━

<b>❌ Путают print и return</b>

<pre><code class="language-python">def get_number():
    print(10)</code></pre>

Такую функцию нельзя использовать для вычислений.

Лучше:

<pre><code class="language-python">def get_number():
    return 10</code></pre>

━━━━━━━━━━━

<b>❌ Забывают вернуть результат</b>

<pre><code class="language-python">def sum_numbers(a, b):
    a + b</code></pre>

Функция вернёт:

<pre><code>None</code></pre>

Нужно:

<pre><code class="language-python">return a + b</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• параметры находятся в определении функции
• аргументы передаются при вызове
• функция может принимать несколько аргументов
• аргументы передаются по порядку
• можно использовать именованные аргументы
• можно задавать значения по умолчанию
• return возвращает результат программе
• после выполнения return функция завершается
• большинство полезных функций принимают аргументы и возвращают результат