<b>⚙️ Урок 6.2. Методы класса и инкапсуляция</b>

<i>В прошлом уроке мы научились создавать классы и объекты. Но пока наши объекты только хранили данные. В этом уроке мы научимся добавлять объектам собственное поведение и познакомимся с одним из главных принципов ООП — инкапсуляцией.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое метод</b>

В обычном программировании мы создаём функции:

<pre><code class="language-python">def say_hello():
    print("Привет")</code></pre>

Функция существует сама по себе.

В ООП функции могут принадлежать объектам.

Такие функции называются:

<pre><code class="language-python">методами</code></pre>

Метод — это функция внутри класса.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Первый метод</b>

Создадим класс пользователя.

<pre><code class="language-python">class User:

    def say_hello(self):
        print("Привет!")</code></pre>

Создадим объект:

<pre><code class="language-python">user = User()</code></pre>

Вызовем метод:

<pre><code class="language-python">user.say_hello()</code></pre>

Результат:

<pre><code>Привет!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 3. Метод использует данные объекта</b>

Методы часто работают с атрибутами объекта.

Пример:

<pre><code class="language-python">class User:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, {self.name}!")</code></pre>

Создание объекта:

<pre><code class="language-python">user = User("Иван")</code></pre>

Вызов:

<pre><code class="language-python">user.greet()</code></pre>

Результат:

<pre><code>Привет, Иван!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Как работает self внутри методов</b>

Когда выполняется:

<pre><code class="language-python">user.greet()</code></pre>

Python автоматически передаёт объект:

<pre><code class="language-python">self = user</code></pre>

Поэтому:

<pre><code class="language-python">self.name</code></pre>

означает:

<pre><code class="language-python">user.name</code></pre>

Именно поэтому self должен быть первым параметром каждого метода.

━━━━━━━━━━━
<b>ЧАСТЬ 5. Методы могут принимать параметры</b>

Методы работают почти так же, как обычные функции.

Пример:

<pre><code class="language-python">class User:

    def greet(self, other_name):
        print(f"Привет, {other_name}!")</code></pre>

Использование:

<pre><code class="language-python">user = User()

user.greet("Анна")</code></pre>

Результат:

<pre><code>Привет, Анна!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 6. Изменение атрибутов через методы</b>

Методы могут менять состояние объекта.

Пример:

<pre><code class="language-python">class Counter:

    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1</code></pre>

Использование:

<pre><code class="language-python">counter = Counter()

counter.increase()
counter.increase()

print(counter.value)</code></pre>

Результат:

<pre><code>2</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Практический пример</b>

Создадим банковский счёт.

<pre><code class="language-python">class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount</code></pre>

Использование:

<pre><code class="language-python">account = BankAccount()

account.deposit(1000)

print(account.balance)</code></pre>

Результат:

<pre><code>1000</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Что такое инкапсуляция</b>

Инкапсуляция — это принцип ООП, который помогает защищать данные объекта от неправильного использования.

Простыми словами:

<b>объект сам управляет своими данными.</b>

Вместо прямого изменения данных мы используем методы.

━━━━━━━━━━━

Не очень хороший вариант:

<pre><code class="language-python">account.balance = -100000</code></pre>

Теперь баланс стал отрицательным.

Это может быть ошибкой.

Лучше изменить данные через метод.

━━━━━━━━━━━
<b>ЧАСТЬ 9. Приватные атрибуты</b>

В Python существуют приватные атрибуты.

Для этого используется двойное подчёркивание:

<pre><code class="language-python">class BankAccount:

    def __init__(self):
        self.__balance = 0</code></pre>

Теперь атрибут считается приватным.

━━━━━━━━━━━

Попытка обратиться напрямую:

<pre><code class="language-python">account.__balance</code></pre>

приведёт к ошибке:

<pre><code>AttributeError</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Работа через методы</b>

Для доступа к приватным данным обычно создают методы.

Пример:

<pre><code class="language-python">class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        return self.__balance</code></pre>

Использование:

<pre><code class="language-python">account = BankAccount()

account.deposit(500)

print(account.show_balance())</code></pre>

Результат:

<pre><code>500</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Одно подчёркивание</b>

Иногда можно встретить:

<pre><code class="language-python">self._balance</code></pre>

Одно подчёркивание означает:

<b>«не трогайте этот атрибут напрямую»</b>

Это соглашение между программистами.

Python не запрещает доступ:

<pre><code class="language-python">account._balance</code></pre>

но считается плохим стилем.

━━━━━━━━━━━
<b>ЧАСТЬ 12. Двойное подчёркивание</b>

Двойное подчёркивание:

<pre><code class="language-python">self.__balance</code></pre>

запускает механизм name mangling.

Python фактически переименовывает поле внутри класса.

Это усложняет случайный доступ к данным.

━━━━━━━━━━━
<b>ЧАСТЬ 13. Методы могут возвращать значения</b>

Метод может работать как функция.

Пример:

<pre><code class="language-python">class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height</code></pre>

Использование:

<pre><code class="language-python">rect = Rectangle(5, 3)

print(rect.area())</code></pre>

Результат:

<pre><code>15</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 14. Объект управляет своим состоянием</b>

Главная идея ООП:

Объект не просто хранит данные.

Он умеет работать с ними самостоятельно.

Пример:

<pre><code class="language-python">class Lamp:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False</code></pre>

Теперь объект сам отвечает за своё состояние.

━━━━━━━━━━━
<b>ЧАСТЬ 15. Типичные ошибки новичков</b>

<b>❌ Забывают self</b>

Неправильно:

<pre><code class="language-python">class User:

    def greet():
        print("Привет")</code></pre>

Правильно:

<pre><code class="language-python">class User:

    def greet(self):
        print("Привет")</code></pre>

━━━━━━━━━━━

<b>❌ Обращаются к атрибуту без self</b>

Неправильно:

<pre><code class="language-python">class User:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(name)</code></pre>

Ошибка:

<pre><code>NameError</code></pre>

Правильно:

<pre><code class="language-python">print(self.name)</code></pre>

━━━━━━━━━━━

<b>❌ Пытаются получить доступ к приватному полю</b>

Неправильно:

<pre><code class="language-python">account.__balance</code></pre>

Используйте специальные методы доступа.

━━━━━━━━━━━

<b>❌ Меняют внутренние данные напрямую</b>

Плохо:

<pre><code class="language-python">account.balance = -1000</code></pre>

Лучше:

<pre><code class="language-python">account.withdraw(1000)</code></pre>

где метод сам выполняет проверки.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• метод — это функция внутри класса
• методы вызываются через объект
• первым параметром метода всегда является self
• методы могут получать параметры
• методы могут возвращать значения
• методы могут изменять состояние объекта
• инкапсуляция помогает защищать данные
• _name — соглашение о «внутреннем» атрибуте
• __name — приватный атрибут
• хороший стиль ООП — работать с данными через методы объекта