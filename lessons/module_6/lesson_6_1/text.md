<b>🏗️ Урок 6.1. Классы и объекты</b>

<i>До этого момента мы работали с числами, строками, списками и функциями. Но большинство современных программ строятся вокруг объектов. В этом уроке вы познакомитесь с объектно-ориентированным программированием (ООП) и научитесь создавать собственные классы.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое ООП</b>

ООП расшифровывается как:

<pre><code>Объектно-Ориентированное Программирование</code></pre>

Это подход к разработке программ, при котором данные и действия объединяются в объекты.

Практически все современные программы используют ООП:

• интернет-магазины  
• банковские системы  
• Telegram-боты  
• игры  
• мобильные приложения  
• веб-сервисы  

ООП помогает создавать большие программы из небольших независимых частей.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Что такое объект</b>

Объект — это сущность, которая имеет:

• характеристики (данные)  
• поведение (действия)

Например, автомобиль:

Характеристики:

• цвет  
• марка  
• скорость  

Действия:

• ехать  
• тормозить  
• сигналить  

В программировании объект работает точно так же.

━━━━━━━━━━━
<b>Примеры объектов</b>

Пользователь:

• имя  
• возраст  
• email  

Действия:

• войти в систему  
• изменить пароль  

━━━━━━━━━━━

Кот:

• кличка  
• возраст  
• вес  

Действия:

• мяукать  
• спать  

━━━━━━━━━━━

Банковский счёт:

• владелец  
• баланс  

Действия:

• пополнить счёт  
• снять деньги  

━━━━━━━━━━━
<b>ЧАСТЬ 3. Что такое класс</b>

Класс — это шаблон для создания объектов.

Представьте чертёж дома.

По одному чертежу можно построить много домов.

В ООП:

• класс = чертёж  
• объект = конкретный дом  

Например:

<pre><code class="language-python">class User:
    pass</code></pre>

Здесь создан класс:

<pre><code class="language-python">User</code></pre>

Но пока объектов нет.

━━━━━━━━━━━
<b>ЧАСТЬ 4. Создание объекта</b>

Объект создаётся вызовом класса.

Пример:

<pre><code class="language-python">class User:
    pass

user1 = User()</code></pre>

Теперь переменная:

<pre><code class="language-python">user1</code></pre>

содержит объект класса User.

Можно создать сколько угодно объектов:

<pre><code class="language-python">user1 = User()
user2 = User()
user3 = User()</code></pre>

Все они будут независимыми.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Атрибуты объекта</b>

Атрибуты — это данные, которые хранятся внутри объекта.

Пример:

<pre><code class="language-python">class User:
    pass

user = User()

user.name = "Иван"
user.age = 25</code></pre>

Получение значений:

<pre><code class="language-python">print(user.name)
print(user.age)</code></pre>

Результат:

<pre><code>Иван
25</code></pre>

━━━━━━━━━━━

Такой способ работает, но используется редко.

Чаще атрибуты создают через специальный метод:

<pre><code class="language-python">__init__()</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Метод __init__()</b>

Метод:

<pre><code class="language-python">__init__()</code></pre>

вызывается автоматически при создании объекта.

Пример:

<pre><code class="language-python">class User:

    def __init__(self):
        print("Создан новый пользователь")

user = User()</code></pre>

Результат:

<pre><code>Создан новый пользователь</code></pre>

Python сам вызывает этот метод после создания объекта.

━━━━━━━━━━━
<b>ЧАСТЬ 7. Передача данных в объект</b>

Обычно через __init__ сразу передают данные.

Пример:

<pre><code class="language-python">class User:

    def __init__(self, name):
        self.name = name</code></pre>

Создание объекта:

<pre><code class="language-python">user = User("Иван")</code></pre>

Теперь внутри объекта хранится имя.

Проверим:

<pre><code class="language-python">print(user.name)</code></pre>

Результат:

<pre><code>Иван</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Что такое self</b>

Новичков чаще всего пугает слово:

<pre><code class="language-python">self</code></pre>

На самом деле всё просто.

self — это ссылка на текущий объект.

Пример:

<pre><code class="language-python">class User:

    def __init__(self, name):
        self.name = name</code></pre>

Когда выполняется:

<pre><code class="language-python">user = User("Иван")</code></pre>

Python подставляет:

<pre><code class="language-python">self = user</code></pre>

Поэтому:

<pre><code class="language-python">self.name</code></pre>

означает:

<pre><code class="language-python">user.name</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Несколько атрибутов</b>

Объект может хранить много данных.

Пример:

<pre><code class="language-python">class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age</code></pre>

Создание:

<pre><code class="language-python">user = User("Иван", 25)</code></pre>

Использование:

<pre><code class="language-python">print(user.name)
print(user.age)</code></pre>

Результат:

<pre><code>Иван
25</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Несколько объектов одного класса</b>

Один класс может создавать множество объектов.

Пример:

<pre><code class="language-python">class User:

    def __init__(self, name):
        self.name = name</code></pre>

Создаём пользователей:

<pre><code class="language-python">user1 = User("Иван")
user2 = User("Анна")
user3 = User("Пётр")</code></pre>

Вывод:

<pre><code class="language-python">print(user1.name)
print(user2.name)
print(user3.name)</code></pre>

Результат:

<pre><code>Иван
Анна
Пётр</code></pre>

Все объекты созданы по одному шаблону.

━━━━━━━━━━━
<b>ЧАСТЬ 11. Практический пример</b>

Создадим класс автомобиля.

<pre><code class="language-python">class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color</code></pre>

Создание объектов:

<pre><code class="language-python">car1 = Car("Toyota", "Красный")
car2 = Car("BMW", "Чёрный")</code></pre>

Получение данных:

<pre><code class="language-python">print(car1.brand)
print(car2.color)</code></pre>

Результат:

<pre><code>Toyota
Чёрный</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Представление объекта в памяти</b>

Когда создаётся объект:

<pre><code class="language-python">user = User("Иван")</code></pre>

в памяти появляется отдельная структура данных.

У каждого объекта свои значения атрибутов.

Поэтому изменение одного объекта не влияет на другой.

Пример:

<pre><code class="language-python">user1 = User("Иван")
user2 = User("Анна")

user1.name = "Пётр"

print(user1.name)
print(user2.name)</code></pre>

Результат:

<pre><code>Пётр
Анна</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 13. Частые ошибки новичков</b>

<b>❌ Забывают self</b>

Неправильно:

<pre><code class="language-python">class User:

    def __init__(name):
        pass</code></pre>

Ошибка.

Правильно:

<pre><code class="language-python">class User:

    def __init__(self, name):
        pass</code></pre>

━━━━━━━━━━━

<b>❌ Путают класс и объект</b>

Неправильно:

<pre><code class="language-python">User.name = "Иван"</code></pre>

Чаще всего нужно работать с объектом:

<pre><code class="language-python">user = User("Иван")</code></pre>

━━━━━━━━━━━

<b>❌ Не передают обязательные параметры</b>

Неправильно:

<pre><code class="language-python">user = User()</code></pre>

если конструктор ожидает:

<pre><code class="language-python">def __init__(self, name):</code></pre>

Возникнет:

<pre><code>TypeError</code></pre>

━━━━━━━━━━━

<b>❌ Используют объект до создания</b>

Неправильно:

<pre><code class="language-python">print(user.name)

user = User("Иван")</code></pre>

Сначала нужно создать объект.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>

• ООП строится вокруг объектов
• объект содержит данные и поведение
• класс — это шаблон для создания объектов
• объект создаётся вызовом класса
• данные объекта называются атрибутами
• метод __init__ вызывается автоматически при создании объекта
• self указывает на текущий объект
• один класс может создавать множество объектов
• каждый объект хранит собственные данные