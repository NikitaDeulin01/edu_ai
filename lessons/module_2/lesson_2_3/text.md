<b>🔄 Урок 2.3. Преобразование типов данных</b>

<i>Очень часто данные нужно переводить из одного типа в другой. Например, input() возвращает строку, но для вычислений нужны числа. В этом уроке вы научитесь преобразовывать типы данных в Python.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Зачем нужно преобразование типов</b>

Представьте:

<pre><code class="language-python">age = input("Введите возраст: ")

print(age + 1)</code></pre>

Если пользователь введёт:

<pre><code>18</code></pre>

программа выдаст ошибку:

<pre><code>TypeError</code></pre>

Почему?

Потому что:

<pre><code class="language-python">input()</code></pre>

всегда возвращает <b>строку (str)</b>.

То есть Python видит:

<pre><code class="language-python">"18" + 1</code></pre>

А строку нельзя сложить с числом.

Нужно преобразование типа.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Преобразование в int</b>

<b>int()</b> превращает значение в целое число.

<pre><code class="language-python">age = int("18")

print(age)
print(type(age))</code></pre>

Результат:

<pre><code>18
&lt;class 'int'&gt;</code></pre>

Теперь можно выполнять вычисления:

<pre><code class="language-python">age = int(input("Возраст: "))

print(age + 1)</code></pre>

━━━━━━━━━━━
<b>Преобразование float → int</b>

<pre><code class="language-python">price = 19.99

print(int(price))</code></pre>

Результат:

<pre><code>19</code></pre>

<b>Важно:</b>

<code>int()</code> не округляет число, а просто отбрасывает дробную часть.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Преобразование в float</b>

<b>float()</b> превращает значение в дробное число.

<pre><code class="language-python">price = float("19.99")

print(price)
print(type(price))</code></pre>

Результат:

<pre><code>19.99
&lt;class 'float'&gt;</code></pre>

<b>Можно преобразовывать int → float:</b>

<pre><code class="language-python">number = 10

print(float(number))</code></pre>

Результат:

<pre><code>10.0</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Преобразование в str</b>

<b>str()</b> превращает значение в строку.

<pre><code class="language-python">age = 25

text = str(age)

print(text)
print(type(text))</code></pre>

Результат:

<pre><code>25
&lt;class 'str'&gt;</code></pre>

<b>Это полезно при выводе текста:</b>

<pre><code class="language-python">age = 25

print("Возраст: " + str(age))</code></pre>

Но сегодня чаще используют <b>f-строки</b>:

<pre><code class="language-python">print(f"Возраст: {age}")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Преобразование в bool</b>

<b>bool()</b> превращает значение в True или False.

<pre><code class="language-python">print(bool(1))
print(bool(0))</code></pre>

Результат:

<pre><code>True
False</code></pre>

━━━━━━━━━━━
<b>Какие значения считаются False</b>

Ложными считаются:

• <code>0</code>  
• <code>0.0</code>  
• <code>""</code>  
• <code>[]</code>  
• <code>{}</code>  
• <code>None</code>  

Всё остальное — True.

<pre><code class="language-python">print(bool(""))
print(bool("Python"))</code></pre>

Результат:

<pre><code>False
True</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Преобразование коллекций</b>

Коллекции тоже можно преобразовывать.

━━━━━━━━━━━
<b>list → tuple</b>

<pre><code class="language-python">numbers = [1, 2, 3]

result = tuple(numbers)

print(result)</code></pre>

Результат:

<pre><code>(1, 2, 3)</code></pre>

━━━━━━━━━━━
<b>tuple → list</b>

<pre><code class="language-python">data = (10, 20, 30)

result = list(data)

print(result)</code></pre>

Результат:

<pre><code>[10, 20, 30]</code></pre>

━━━━━━━━━━━
<b>list → set</b>

Очень полезно для удаления повторений.

<pre><code class="language-python">numbers = [1, 1, 2, 2, 3]

unique = set(numbers)

print(unique)</code></pre>

Результат:

<pre><code>{1, 2, 3}</code></pre>

━━━━━━━━━━━
<b>set → list</b>

<pre><code class="language-python">numbers = {1, 2, 3}

result = list(numbers)

print(result)</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Ошибки преобразования</b>

Не любое значение можно преобразовать.

Например:

<pre><code class="language-python">number = int("hello")</code></pre>

Ошибка:

<pre><code>ValueError</code></pre>

Потому что строка <code>"hello"</code> не является числом.

━━━━━━━━━━━
<b>Ещё пример:</b>

<pre><code class="language-python">price = float("abc")</code></pre>

Тоже ошибка.

Поэтому программа должна получать корректные данные.

━━━━━━━━━━━
<b>ЧАСТЬ 8. Полезные примеры</b>
<b>Сумма двух чисел:</b>

<pre><code class="language-python">a = int(input("Первое число: "))
b = int(input("Второе число: "))

print(f"Сумма: {a + b}")</code></pre>

━━━━━━━━━━━

<b>Площадь прямоугольника:</b>

<pre><code class="language-python">width = float(input("Ширина: "))
height = float(input("Высота: "))

print(f"Площадь: {width * height}")</code></pre>

━━━━━━━━━━━

<b>Удаление повторений:</b>

<pre><code class="language-python">numbers = [1, 1, 2, 2, 3]

unique = list(set(numbers))

print(unique)</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Частые ошибки новичков</b>

<b>❌ Забывают int()</b>

<pre><code class="language-python">a = input("Число: ")

print(a + 1)</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

━━━━━━━━━━━

<b>❌ Пытаются преобразовать текст в число</b>

<pre><code class="language-python">int("Привет")</code></pre>

Ошибка:

<pre><code>ValueError</code></pre>


<b>❌ Путают list и set</b>

<pre><code class="language-python">numbers = {1, 2, 3}

print(numbers[0])</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

У множества нет индексов.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• <code>int()</code> — преобразование в целое число  
• <code>float()</code> — преобразование в дробное число  
• <code>str()</code> — преобразование в строку  
• <code>bool()</code> — преобразование в True / False  
• <code>input()</code> всегда возвращает строку  
• list, tuple и set можно преобразовывать друг в друга  
• неправильное преобразование вызывает <code>ValueError</code>