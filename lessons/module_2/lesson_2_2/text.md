<b>🗂️ Урок 2.2. Коллекции данных: list, tuple, set, dict</b>

<i>Обычной переменной можно хранить только одно значение. Но очень часто нужно хранить сразу много данных: список покупок, оценки, пользователей, настройки. Для этого в Python существуют коллекции.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое коллекции</b>

<b>Коллекция</b> — это объект, который хранит несколько значений сразу.

Например:

<pre><code class="language-python">names = ["Анна", "Иван", "Мария"]</code></pre>

Здесь в одной переменной хранится сразу несколько имён.

В Python есть 4 основные коллекции:

• <code>list</code> — список  
• <code>tuple</code> — кортеж  
• <code>set</code> — множество  
• <code>dict</code> — словарь  

━━━━━━━━━━━
<b>ЧАСТЬ 2. Списки (list)</b>

<b>list</b> — упорядоченная изменяемая коллекция.

Создаётся через квадратные скобки:

<pre><code class="language-python">numbers = [1, 2, 3, 4]
names = ["Анна", "Иван", "Мария"]</code></pre>

<b>Список может хранить разные типы данных:</b>

<pre><code class="language-python">data = [10, "Python", True, 3.14]</code></pre>

━━━━━━━━━━━
<b>Индексы списка</b>

У каждого элемента есть индекс.

Индексация начинается с 0.

<pre><code class="language-python">names = ["Анна", "Иван", "Мария"]

print(names[0])
print(names[1])</code></pre>

Результат:

<pre><code>Анна
Иван</code></pre>

<b>Отрицательные индексы</b> идут с конца:

<pre><code class="language-python">print(names[-1])</code></pre>

Результат:

<pre><code>Мария</code></pre>

━━━━━━━━━━━
<b>Списки изменяемые</b>

Элементы можно менять:

<pre><code class="language-python">numbers = [1, 2, 3]

numbers[0] = 100

print(numbers)</code></pre>

Результат:

<pre><code>[100, 2, 3]</code></pre>

━━━━━━━━━━━
<b>Методы списков</b>

<b>Добавление элемента:</b>

<pre><code class="language-python">numbers = [1, 2]

numbers.append(3)

print(numbers)</code></pre>

Результат:

<pre><code>[1, 2, 3]</code></pre>

<b>Удаление элемента:</b>

<pre><code class="language-python">numbers.remove(2)</code></pre>

<b>Длина списка:</b>

<pre><code class="language-python">print(len(numbers))</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 3. Кортежи (tuple)</b>

<b>tuple</b> — упорядоченная НЕизменяемая коллекция.

Создаётся через круглые скобки:

<pre><code class="language-python">point = (10, 20)
rgb = (255, 128, 0)</code></pre>

<b>Кортеж похож на список</b>, но его нельзя изменять.

<pre><code class="language-python">point = (10, 20)

# point[0] = 50
# TypeError</code></pre>

━━━━━━━━━━━
<b>Когда используют tuple</b>

Кортежи используют:
• для неизменяемых данных  
• координат  
• настроек  
• фиксированных наборов значений  

<b>Можно получать элементы по индексу:</b>

<pre><code class="language-python">rgb = (255, 128, 0)

print(rgb[1])</code></pre>

Результат:

<pre><code>128</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Множества (set)</b>

<b>set</b> — неупорядоченная коллекция уникальных элементов.

Создаётся через фигурные скобки:

<pre><code class="language-python">numbers = {1, 2, 3, 4}</code></pre>

<b>Главная особенность:</b>

В множестве не может быть повторений.

<pre><code class="language-python">numbers = {1, 1, 1, 2, 2, 3}

print(numbers)</code></pre>

Результат:

<pre><code>{1, 2, 3}</code></pre>

━━━━━━━━━━━
<b>Элементы в set не имеют индексов</b>

Нельзя написать:

<pre><code class="language-python">numbers[0]</code></pre>

Потому что множество не хранит порядок элементов.

━━━━━━━━━━━
<b>Методы set</b>

<b>Добавление:</b>

<pre><code class="language-python">numbers.add(10)</code></pre>

<b>Удаление:</b>

<pre><code class="language-python">numbers.remove(2)</code></pre>

<b>Проверка наличия:</b>

<pre><code class="language-python">print(3 in numbers)</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Словари (dict)</b>

<b>dict</b> — коллекция пар ключ-значение.

Создаётся через фигурные скобки:

<pre><code class="language-python">user = {
    "name": "Анна",
    "age": 25,
    "city": "Москва"
}</code></pre>

Здесь:
• <code>"name"</code> — ключ  
• <code>"Анна"</code> — значение  

━━━━━━━━━━━
<b>Получение значений</b>

<pre><code class="language-python">print(user["name"])
print(user["age"])</code></pre>

Результат:

<pre><code>Анна
25</code></pre>

━━━━━━━━━━━
<b>Изменение словаря</b>

<pre><code class="language-python">user["age"] = 30

print(user)</code></pre>

<b>Добавление новых данных:</b>

<pre><code class="language-python">user["country"] = "Россия"</code></pre>

━━━━━━━━━━━
<b>Полезные методы dict</b>

<b>Все ключи:</b>

<pre><code class="language-python">print(user.keys())</code></pre>

<b>Все значения:</b>

<pre><code class="language-python">print(user.values())</code></pre>

<b>Все пары:</b>

<pre><code class="language-python">print(user.items())</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Сравнение коллекций</b>

<table>
<tr>
<td><b>Тип</b></td>
<td><b>Изменяемый</b></td>
<td><b>Порядок</b></td>
<td><b>Уникальность</b></td>
</tr>

<tr>
<td>list</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>

<tr>
<td>tuple</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>

<tr>
<td>set</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>

<tr>
<td>dict</td>
<td>✅</td>
<td>✅</td>
<td>ключи уникальны</td>
</tr>
</table>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Частые ошибки новичков</b>

<b>❌ Путают list и tuple</b>

<pre><code class="language-python">data = (1, 2, 3)

data[0] = 10</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

Потому что tuple неизменяемый.

━━━━━━━━━━━

<b>❌ Используют индекс у set</b>

<pre><code class="language-python">numbers = {1, 2, 3}

print(numbers[0])</code></pre>

Ошибка:

<pre><code>TypeError</code></pre>

У set нет индексов.

━━━━━━━━━━━

<b>❌ Обращаются к несуществующему ключу</b>

<pre><code class="language-python">user = {"name": "Анна"}

print(user["age"])</code></pre>

Ошибка:

<pre><code>KeyError</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• <code>list</code> — изменяемый список  
• <code>tuple</code> — неизменяемый список  
• <code>set</code> хранит только уникальные значения  
• у <code>set</code> нет индексов  
• <code>dict</code> хранит пары ключ-значение  
• элементы list и tuple получают по индексу  
• элементы dict получают по ключу  