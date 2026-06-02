<b>🧬 Урок 6.3. Наследование и полиморфизм</b>

<i>В предыдущих уроках вы научились создавать собственные классы и добавлять им данные и методы. Но что делать, если несколько классов очень похожи друг на друга? Чтобы не копировать один и тот же код, в ООП используется наследование.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Зачем нужно наследование</b>

Представьте, что у нас есть несколько животных:

• Собака  
• Кошка  
• Попугай  

У всех есть:

• имя  
• возраст  
• метод издать звук  

Можно создать отдельный класс для каждого животного.

Но тогда придётся дублировать много одинакового кода.

Наследование позволяет вынести общую логику в один класс.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Родительский и дочерний классы</b>

В ООП существуют:

• родительский класс (базовый класс)  
• дочерний класс (производный класс)

Родитель содержит общую функциональность.

Дочерние классы получают её автоматически.

━━━━━━━━━━━
<b>Первый пример</b>

Создадим базовый класс:

<pre><code class="language-python">class Animal:

    def eat(self):
        print("Животное ест")</code></pre>

Теперь создадим дочерний класс:

<pre><code class="language-python">class Dog(Animal):
    pass</code></pre>

Создание объекта:

<pre><code class="language-python">dog = Dog()

dog.eat()</code></pre>

Результат:

<pre><code>Животное ест</code></pre>

Хотя метод находится в классе Animal.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Что получает дочерний класс</b>

Дочерний класс автоматически наследует:

✅ методы

✅ атрибуты

✅ большую часть логики родителя

Пример:

<pre><code class="language-python">class Animal:

    def sleep(self):
        print("Спит")

class Cat(Animal):
    pass</code></pre>

Использование:

<pre><code class="language-python">cat = Cat()

cat.sleep()</code></pre>

Результат:

<pre><code>Спит</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 4. Собственные методы дочернего класса</b>

Дочерний класс может добавлять новые возможности.

Пример:

<pre><code class="language-python">class Animal:

    def eat(self):
        print("Ест")

class Dog(Animal):

    def bark(self):
        print("Гав!")</code></pre>

Использование:

<pre><code class="language-python">dog = Dog()

dog.eat()
dog.bark()</code></pre>

Результат:

<pre><code>Ест
Гав!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Переопределение методов</b>

Иногда дочерний класс должен вести себя по-другому.

Для этого используется переопределение метода.

Пример:

<pre><code class="language-python">class Animal:

    def speak(self):
        print("Какой-то звук")

class Dog(Animal):

    def speak(self):
        print("Гав!")</code></pre>

Использование:

<pre><code class="language-python">dog = Dog()

dog.speak()</code></pre>

Результат:

<pre><code>Гав!</code></pre>

Метод родителя был заменён методом дочернего класса.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Несколько дочерних классов</b>

Один родитель может иметь много потомков.

Пример:

<pre><code class="language-python">class Animal:

    def speak(self):
        print("Звук")</code></pre>

━━━━━━━━━━━

Собака:

<pre><code class="language-python">class Dog(Animal):

    def speak(self):
        print("Гав!")</code></pre>

━━━━━━━━━━━

Кошка:

<pre><code class="language-python">class Cat(Animal):

    def speak(self):
        print("Мяу!")</code></pre>

━━━━━━━━━━━

Попугай:

<pre><code class="language-python">class Parrot(Animal):

    def speak(self):
        print("Привет!")</code></pre>

━━━━━━━━━━━

Использование:

<pre><code class="language-python">dog = Dog()
cat = Cat()
parrot = Parrot()

dog.speak()
cat.speak()
parrot.speak()</code></pre>

Результат:

<pre><code>Гав!
Мяу!
Привет!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Что такое super()</b>

Иногда нужно вызвать метод родительского класса.

Для этого используется:

<pre><code class="language-python">super()</code></pre>

Пример:

<pre><code class="language-python">class Animal:

    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):

    def speak(self):
        super().speak()
        print("Гав!")</code></pre>

Использование:

<pre><code class="language-python">dog = Dog()

dog.speak()</code></pre>

Результат:

<pre><code>Животное издаёт звук
Гав!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. super() и __init__()</b>

Очень часто super() используется в конструкторах.

Родитель:

<pre><code class="language-python">class Animal:

    def __init__(self, name):
        self.name = name</code></pre>

Дочерний класс:

<pre><code class="language-python">class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed</code></pre>

Создание объекта:

<pre><code class="language-python">dog = Dog("Шарик", "Овчарка")</code></pre>

Теперь объект содержит:

<pre><code class="language-python">dog.name
dog.breed</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Что такое полиморфизм</b>

Полиморфизм — это способность разных объектов одинаково реагировать на один и тот же вызов.

Звучит сложно.

На практике всё проще.

━━━━━━━━━━━

Есть классы:

<pre><code class="language-python">class Dog:

    def speak(self):
        print("Гав!")</code></pre>

<pre><code class="language-python">class Cat:

    def speak(self):
        print("Мяу!")</code></pre>

━━━━━━━━━━━

Теперь создадим список:

<pre><code class="language-python">animals = [
    Dog(),
    Cat()
]</code></pre>

Цикл:

<pre><code class="language-python">for animal in animals:
    animal.speak()</code></pre>

Результат:

<pre><code>Гав!
Мяу!</code></pre>

Мы вызываем один и тот же метод:

<pre><code class="language-python">speak()</code></pre>

но каждый объект выполняет свою реализацию.

Это и есть полиморфизм.

━━━━━━━━━━━
<b>ЧАСТЬ 10. isinstance()</b>

Иногда нужно проверить тип объекта.

Для этого используется:

<pre><code class="language-python">isinstance()</code></pre>

Пример:

<pre><code class="language-python">dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))</code></pre>

Результат:

<pre><code>True
True</code></pre>

Потому что Dog наследуется от Animal.

━━━━━━━━━━━
<b>ЧАСТЬ 11. Практический пример</b>

Создадим систему сотрудников.

Родитель:

<pre><code class="language-python">class Employee:

    def work(self):
        print("Работает")</code></pre>

━━━━━━━━━━━

Программист:

<pre><code class="language-python">class Developer(Employee):

    def work(self):
        print("Пишет код")</code></pre>

━━━━━━━━━━━

Дизайнер:

<pre><code class="language-python">class Designer(Employee):

    def work(self):
        print("Рисует интерфейс")</code></pre>

━━━━━━━━━━━

Использование:

<pre><code class="language-python">employees = [
    Developer(),
    Designer()
]

for employee in employees:
    employee.work()</code></pre>

Результат:

<pre><code>Пишет код
Рисует интерфейс</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Когда использовать наследование</b>

Подходит, если между объектами есть отношение:

<b>"является"</b>

Примеры:

• Собака является животным

• Кошка является животным

• Программист является сотрудником

• Студент является человеком

━━━━━━━━━━━

Не стоит использовать наследование только ради экономии нескольких строк кода.

━━━━━━━━━━━
<b>ЧАСТЬ 13. Типичные ошибки новичков</b>

<b>❌ Забывают указать родителя</b>

Неправильно:

<pre><code class="language-python">class Dog:
    pass</code></pre>

Правильно:

<pre><code class="language-python">class Dog(Animal):
    pass</code></pre>

━━━━━━━━━━━

<b>❌ Не вызывают super().__init__()</b>

Неправильно:

<pre><code class="language-python">class Dog(Animal):

    def __init__(self, name):
        pass</code></pre>

Атрибуты родителя не будут созданы.

━━━━━━━━━━━

<b>❌ Путают наследование и объекты</b>

Неправильно:

<pre><code class="language-python">dog = Animal()</code></pre>

если нужен объект собаки.

Нужно:

<pre><code class="language-python">dog = Dog()</code></pre>

━━━━━━━━━━━

<b>❌ Создают слишком длинные цепочки наследования</b>

Плохо:

<pre><code class="language-python">A → B → C → D → E → F</code></pre>

Такой код сложно поддерживать.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• наследование позволяет создавать классы на основе других классов
• родительский класс содержит общую логику
• дочерний класс получает методы и атрибуты родителя
• дочерний класс может добавлять собственные методы
• методы родителя можно переопределять
• super() позволяет обращаться к логике родителя
• полиморфизм — это единый интерфейс для разных объектов
• isinstance() проверяет принадлежность объекта к классу
• наследование помогает уменьшать дублирование кода