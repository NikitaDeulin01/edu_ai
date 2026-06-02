<b>🔀 Урок 3.1. Условная конструкция. Оператор if</b>

<i>Программы становятся по-настоящему полезными, когда умеют принимать решения. В этом уроке вы научитесь проверять условия и управлять поведением программы с помощью if.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое условие</b>

Программа может выполнять разные действия в зависимости от ситуации.

Например:

• если пользователь ввёл правильный пароль → разрешить вход  
• если число больше 0 → вывести одно сообщение  
• если идёт дождь → взять зонт  

Для этого используются <b>условные конструкции</b>.

Главная конструкция в Python:

<pre><code class="language-python">if</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 2. Оператор if</b>

Простейший пример:

<pre><code class="language-python">age = 20

if age >= 18:
    print("Вы совершеннолетний")</code></pre>

Если условие истинно (<code>True</code>), код внутри блока выполняется.

Если условие ложно (<code>False</code>) — блок пропускается.

━━━━━━━━━━━
<b>Как работает if</b>

Python:
1. проверяет условие  
2. получает True или False  
3. решает — выполнять блок или нет  

<pre><code class="language-python">temperature = 25

if temperature > 20:
    print("Сегодня тепло")</code></pre>

Условие:

<pre><code class="language-python">temperature > 20</code></pre>

вернёт:

<pre><code class="language-python">True</code></pre>

поэтому код выполнится.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Отступы в Python</b>

В Python блоки кода определяются <b>отступами</b>.

<pre><code class="language-python">if True:
    print("Первый")
    print("Второй")

print("Третий")</code></pre>

Результат:

<pre><code>Первый
Второй
Третий</code></pre>

<b>Важно:</b>

• обычно используют 4 пробела  
• одинаковый блок → одинаковый отступ  
• без отступа будет ошибка  

━━━━━━━━━━━
<b>ЧАСТЬ 4. Оператор else</b>

<b>else</b> выполняется, если условие ложно.

<pre><code class="language-python">age = 16

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")</code></pre>

Результат:

<pre><code>Доступ запрещён</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Оператор elif</b>

Иногда вариантов больше двух.

Для этого используют <b>elif</b>.

<pre><code class="language-python">temperature = 10

if temperature < 0:
    print("Очень холодно")
elif temperature < 20:
    print("Прохладно")
else:
    print("Тепло")</code></pre>

Python проверяет условия сверху вниз.

Как только находится первое True — остальные проверки пропускаются.

━━━━━━━━━━━
<b>Порядок условий важен</b>

❌ Неправильно:

<pre><code class="language-python">temperature = 5

if temperature < 20:
    print("Прохладно")
elif temperature < 0:
    print("Очень холодно")</code></pre>

Вторая проверка никогда не выполнится.

Потому что:

<pre><code class="language-python">temperature < 20</code></pre>

уже True.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Операторы сравнения</b>

В условиях часто используются сравнения.

<table>
<tr>
<td><b>Оператор</b></td>
<td><b>Описание</b></td>
</tr>

<tr>
<td>==</td>
<td>равно</td>
</tr>

<tr>
<td>!=</td>
<td>не равно</td>
</tr>

<tr>
<td>&gt;</td>
<td>больше</td>
</tr>

<tr>
<td>&lt;</td>
<td>меньше</td>
</tr>

<tr>
<td>&gt;=</td>
<td>больше или равно</td>
</tr>

<tr>
<td>&lt;=</td>
<td>меньше или равно</td>
</tr>
</table>

Пример:

<pre><code class="language-python">score = 90

if score >= 60:
    print("Экзамен сдан")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Логические операторы</b>

Для сложных условий используют:

• <code>and</code> — И  
• <code>or</code> — ИЛИ  
• <code>not</code> — НЕ  

━━━━━━━━━━━
<b>Оператор and</b>

Условие True, если истинны ОБА выражения.

<pre><code class="language-python">age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Можно войти")</code></pre>

━━━━━━━━━━━
<b>Оператор or</b>

True, если истинно хотя бы одно выражение.

<pre><code class="language-python">day = "суббота"

if day == "суббота" or day == "воскресенье":
    print("Выходной")</code></pre>

━━━━━━━━━━━
<b>Оператор not</b>

Инвертирует значение.

<pre><code class="language-python">is_banned = False

if not is_banned:
    print("Доступ разрешён")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Python-стиль</b>

━━━━━━━━━━━
<b>Truthy и Falsy</b>

В Python можно писать короткие проверки.

❌ Новички часто пишут:

<pre><code class="language-python">if is_admin == True:</code></pre>

✅ Pythonic-вариант:

<pre><code class="language-python">if is_admin:</code></pre>

━━━━━━━━━━━

❌ Проверка пустой строки:

<pre><code class="language-python">if name == "":</code></pre>

✅ Лучше:

<pre><code class="language-python">if not name:</code></pre>

━━━━━━━━━━━
<b>Оператор in</b>

Вместо длинного or:

<pre><code class="language-python">if day == "суббота" or day == "воскресенье":</code></pre>

лучше:

<pre><code class="language-python">if day in ("суббота", "воскресенье"):</code></pre>

━━━━━━━━━━━
<b>Проверка диапазона</b>

❌ Обычный вариант:

<pre><code class="language-python">if x >= 0 and x < 100:</code></pre>

✅ Pythonic-вариант:

<pre><code class="language-python">if 0 <= x < 100:</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Тернарный оператор</b>

Для коротких условий используют тернарный оператор.

Обычный вариант:

<pre><code class="language-python">age = 20

if age >= 18:
    status = "совершеннолетний"
else:
    status = "несовершеннолетний"</code></pre>

Короткая запись:

<pre><code class="language-python">status = "совершеннолетний" if age >= 18 else "несовершеннолетний"</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Практические примеры</b>

<b>Проверка чётности:</b>

<pre><code class="language-python">number = 42

if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")</code></pre>

━━━━━━━━━━━

<b>Проверка пароля:</b>

<pre><code class="language-python">password = "qwerty123"

if len(password) < 8:
    print("Пароль слишком короткий")
else:
    print("Пароль подходит")</code></pre>

━━━━━━━━━━━

<b>Проверка возраста:</b>

<pre><code class="language-python">age = int(input("Возраст: "))

if age >= 18:
    print("Вход разрешён")
else:
    print("Вход запрещён")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Частые ошибки новичков</b>

<b>❌ Путают = и ==</b>

<pre><code class="language-python">if age = 18:</code></pre>

Ошибка.

<b>=</b> — присваивание  
<b>==</b> — сравнение  

✅ Правильно:

<pre><code class="language-python">if age == 18:</code></pre>

━━━━━━━━━━━

<b>❌ Забывают двоеточие</b>

<pre><code class="language-python">if age > 18</code></pre>

После условия всегда нужен символ <code>:</code>

━━━━━━━━━━━

<b>❌ Ошибки с отступами</b>

<pre><code class="language-python">if True:
print("Hello")</code></pre>

Будет:

<pre><code>IndentationError</code></pre>

━━━━━━━━━━━

<b>❌ Путают порядок условий</b>

<pre><code class="language-python">if x < 100:
    ...
elif x < 10:
    ...</code></pre>

Вторая проверка никогда не выполнится.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• <code>if</code> проверяет условие  
• <code>else</code> выполняется при False  
• <code>elif</code> нужен для нескольких вариантов  
• блоки кода определяются отступами  
• <code>==</code> — сравнение  
• <code>=</code> — присваивание  
• <code>and</code>, <code>or</code>, <code>not</code> позволяют строить сложные условия  
• Python проверяет условия сверху вниз
