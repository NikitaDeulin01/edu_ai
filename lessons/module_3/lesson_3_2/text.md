<b>🔁 Урок 3.2. Итерации и циклы</b>

<i>Циклы позволяют выполнять код много раз без копирования одних и тех же строк. Это один из важнейших инструментов программирования.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое цикл</b>

<b>Цикл</b> — конструкция, которая повторяет выполнение блока кода.

Например:

• вывести числа от 1 до 10  
• пройтись по списку  
• обработать каждый символ строки  
• повторять действие, пока условие истинно  

Без циклов пришлось бы писать:

<pre><code class="language-python">print(1)
print(2)
print(3)
print(4)
print(5)</code></pre>

Циклы делают это автоматически.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Цикл for</b>

<b>for</b> используется для перебора элементов последовательности.

Пример:

<pre><code class="language-python">fruits = ["яблоко", "банан", "вишня"]

for fruit in fruits:
    print(fruit)</code></pre>

Результат:

<pre><code>яблоко
банан
вишня</code></pre>

Python:
1. берёт элемент  
2. сохраняет его в переменную  
3. выполняет код внутри цикла  
4. переходит к следующему элементу  

━━━━━━━━━━━
<b>ЧАСТЬ 3. Функция range()</b>

Очень часто цикл нужен определённое количество раз.

Для этого используется <b>range()</b>.

<pre><code class="language-python">for i in range(5):
    print(i)</code></pre>

Результат:

<pre><code>0
1
2
3
4</code></pre>

━━━━━━━━━━━
<b>Как работает range()</b>

<b>range(stop)</b>

<pre><code class="language-python">range(5)</code></pre>

создаёт числа:

<pre><code>0 1 2 3 4</code></pre>

━━━━━━━━━━━

<b>range(start, stop)</b>

<pre><code class="language-python">for i in range(2, 6):
    print(i)</code></pre>

Результат:

<pre><code>2
3
4
5</code></pre>

━━━━━━━━━━━

<b>range(start, stop, step)</b>

<pre><code class="language-python">for i in range(0, 10, 2):
    print(i)</code></pre>

Результат:

<pre><code>0
2
4
6
8</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Перебор строк</b>

Строки тоже можно перебирать.

<pre><code class="language-python">word = "Python"

for char in word:
    print(char)</code></pre>

Результат:

<pre><code>P
y
t
h
o
n</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Функция enumerate()</b>

Иногда нужен и элемент, и его индекс.

Для этого используют <b>enumerate()</b>.

<pre><code class="language-python">fruits = ["яблоко", "банан", "вишня"]

for index, fruit in enumerate(fruits):
    print(index, fruit)</code></pre>

Результат:

<pre><code>0 яблоко
1 банан
2 вишня</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Цикл while</b>

<b>while</b> выполняется, пока условие True.

<pre><code class="language-python">count = 1

while count <= 5:
    print(count)
    count += 1</code></pre>

Результат:

<pre><code>1
2
3
4
5</code></pre>

━━━━━━━━━━━
<b>Важно менять условие</b>

Вот опасный код:

<pre><code class="language-python">count = 1

while count <= 5:
    print(count)</code></pre>

Переменная count никогда не меняется.

Цикл станет <b>бесконечным</b>.

━━━━━━━━━━━
<b>ЧАСТЬ 7. break</b>

<b>break</b> полностью останавливает цикл.

<pre><code class="language-python">for i in range(10):
    if i == 5:
        break

    print(i)</code></pre>

Результат:

<pre><code>0
1
2
3
4</code></pre>

Когда i становится 5 — цикл завершается.

━━━━━━━━━━━
<b>ЧАСТЬ 8. continue</b>

<b>continue</b> пропускает текущую итерацию.

<pre><code class="language-python">for i in range(6):
    if i == 3:
        continue

    print(i)</code></pre>

Результат:

<pre><code>0
1
2
4
5</code></pre>

Число 3 пропущено.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Вложенные циклы</b>

Циклы можно вкладывать друг в друга.

<pre><code class="language-python">for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)</code></pre>

Результат:

<pre><code>1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. List Comprehension</b>

Python позволяет создавать списки в одну строку.

Обычный способ:

<pre><code class="language-python">squares = []

for i in range(5):
    squares.append(i ** 2)</code></pre>

Pythonic-вариант:

<pre><code class="language-python">squares = [i ** 2 for i in range(5)]</code></pre>

Результат:

<pre><code>[0, 1, 4, 9, 16]</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Частые ошибки новичков</b>

<b>❌ Забывают двоеточие</b>

<pre><code class="language-python">for i in range(5)</code></pre>

Нужно:

<pre><code class="language-python">for i in range(5):</code></pre>

━━━━━━━━━━━

<b>❌ Ошибки с отступами</b>

<pre><code class="language-python">for i in range(5):
print(i)</code></pre>

Будет:

<pre><code>IndentationError</code></pre>

━━━━━━━━━━━

<b>❌ Бесконечный while</b>

<pre><code class="language-python">while True:
    print("Hello")</code></pre>

Цикл никогда не закончится.

━━━━━━━━━━━

<b>❌ Путают break и continue</b>

• <code>break</code> — остановить цикл  
• <code>continue</code> — пропустить итерацию  

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• <code>for</code> перебирает элементы  
• <code>while</code> работает, пока условие True  
• <code>range()</code> создаёт диапазон чисел  
• <code>break</code> останавливает цикл  
• <code>continue</code> пропускает итерацию  
• строки и списки можно перебирать  
• циклы используют отступы