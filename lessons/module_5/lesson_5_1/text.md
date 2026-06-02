<b>⚠️ Урок 5.1. Обработка исключений (try, except)</b>

<i>Любая программа рано или поздно сталкивается с ошибками. Пользователь может ввести неправильные данные, файл может отсутствовать, а число может оказаться нулём. В этом уроке вы научитесь обрабатывать ошибки и делать программы устойчивыми к сбоям.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое исключение</b>

Во время выполнения программы могут возникать ошибки.

Например:

• пользователь ввёл текст вместо числа  
• программа пытается открыть несуществующий файл  
• происходит деление на ноль  

Такие ошибки называются:

<pre><code class="language-python">исключениями (exceptions)</code></pre>

Пример:

<pre><code class="language-python">number = int("abc")</code></pre>

Результат:

<pre><code>ValueError:
invalid literal for int()</code></pre>

Программа аварийно завершится.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Зачем нужна обработка ошибок</b>

Без обработки ошибок программа может неожиданно остановиться.

Пример:

<pre><code class="language-python">age = int(input("Введите возраст: "))

print(age)</code></pre>

Если пользователь введёт:

<pre><code>двадцать</code></pre>

возникнет ошибка и программа завершится.

Более профессиональный подход — перехватить ошибку и показать понятное сообщение.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Конструкция try-except</b>

Основной инструмент обработки ошибок:

<pre><code class="language-python">try:
    опасный код
except:
    обработка ошибки</code></pre>

Пример:

<pre><code class="language-python">try:
    age = int(input("Возраст: "))
    print(age)
except:
    print("Нужно ввести число")</code></pre>

Если пользователь введёт:

<pre><code>abc</code></pre>

Результат:

<pre><code>Нужно ввести число</code></pre>

Программа не завершится аварийно.

━━━━━━━━━━━
<b>Как работает try-except</b>

Python выполняет код внутри:

<pre><code class="language-python">try</code></pre>

Если ошибки нет:

✅ выполняется код дальше

Если ошибка возникла:

✅ Python переходит в блок

<pre><code class="language-python">except</code></pre>

и выполняет его.

━━━━━━━━━━━
<b>ЧАСТЬ 4. Обработка конкретных ошибок</b>

Плохая практика:

<pre><code class="language-python">except:</code></pre>

Лучше указывать конкретный тип ошибки.

Пример:

<pre><code class="language-python">try:
    number = int(input())
except ValueError:
    print("Введено не число")</code></pre>

Теперь программа ловит только:

<pre><code class="language-python">ValueError</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Самые распространённые исключения</b>

<table>
<tr>
<td><b>Ошибка</b></td>
<td><b>Описание</b></td>
</tr>

<tr>
<td>ValueError</td>
<td>Неверное значение</td>
</tr>

<tr>
<td>TypeError</td>
<td>Неверный тип данных</td>
</tr>

<tr>
<td>ZeroDivisionError</td>
<td>Деление на ноль</td>
</tr>

<tr>
<td>IndexError</td>
<td>Неверный индекс списка</td>
</tr>

<tr>
<td>KeyError</td>
<td>Ключ отсутствует в словаре</td>
</tr>

<tr>
<td>FileNotFoundError</td>
<td>Файл не найден</td>
</tr>
</table>

━━━━━━━━━━━
<b>ЧАСТЬ 6. ZeroDivisionError</b>

Пример ошибки:

<pre><code class="language-python">print(10 / 0)</code></pre>

Результат:

<pre><code>ZeroDivisionError</code></pre>

Обработка:

<pre><code class="language-python">try:
    result = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 7. ValueError</b>

Пример:

<pre><code class="language-python">number = int("abc")</code></pre>

Ошибка:

<pre><code>ValueError</code></pre>

Обработка:

<pre><code class="language-python">try:
    number = int("abc")
except ValueError:
    print("Строку нельзя преобразовать в число")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. IndexError</b>

Список:

<pre><code class="language-python">numbers = [10, 20, 30]</code></pre>

Ошибка:

<pre><code class="language-python">print(numbers[5])</code></pre>

Результат:

<pre><code>IndexError</code></pre>

Обработка:

<pre><code class="language-python">try:
    print(numbers[5])
except IndexError:
    print("Такого элемента нет")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. KeyError</b>

Словарь:

<pre><code class="language-python">user = {
    "name": "Иван"
}</code></pre>

Ошибка:

<pre><code class="language-python">print(user["age"])</code></pre>

Результат:

<pre><code>KeyError</code></pre>

Обработка:

<pre><code class="language-python">try:
    print(user["age"])
except KeyError:
    print("Такого ключа нет")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 10. Несколько except</b>

Одна программа может обрабатывать разные ошибки.

Пример:

<pre><code class="language-python">try:
    number = int(input())
    result = 10 / number

except ValueError:
    print("Введите число")

except ZeroDivisionError:
    print("Деление на ноль запрещено")</code></pre>

Python выберет нужный блок автоматически.

━━━━━━━━━━━
<b>ЧАСТЬ 11. Получение текста ошибки</b>

Иногда полезно узнать подробности ошибки.

Используется:

<pre><code class="language-python">as</code></pre>

Пример:

<pre><code class="language-python">try:
    number = int("abc")

except ValueError as error:
    print(error)</code></pre>

Результат:

<pre><code>invalid literal for int()</code></pre>

Переменная:

<pre><code class="language-python">error</code></pre>

содержит объект ошибки.

━━━━━━━━━━━
<b>ЧАСТЬ 12. Блок else</b>

Блок:

<pre><code class="language-python">else</code></pre>

выполняется только если ошибки не было.

Пример:

<pre><code class="language-python">try:
    number = int(input())
except ValueError:
    print("Ошибка")
else:
    print("Число успешно получено")</code></pre>

Если исключение возникло — else пропускается.

━━━━━━━━━━━
<b>ЧАСТЬ 13. Блок finally</b>

Блок:

<pre><code class="language-python">finally</code></pre>

выполняется всегда.

Даже если произошла ошибка.

Пример:

<pre><code class="language-python">try:
    number = int(input())
except ValueError:
    print("Ошибка")
finally:
    print("Работа программы завершена")</code></pre>

Этот блок часто используют для:

• закрытия файлов

• освобождения ресурсов

• очистки данных

━━━━━━━━━━━
<b>ЧАСТЬ 14. Полная конструкция</b>

Можно использовать все блоки сразу.

<pre><code class="language-python">try:
    number = int(input())

except ValueError:
    print("Ошибка")

else:
    print("Успех")

finally:
    print("Конец программы")</code></pre>

Порядок всегда такой:

<pre><code class="language-python">try
except
else
finally</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 15. Генерация собственных ошибок</b>

Иногда нужно специально вызвать исключение.

Для этого используется:

<pre><code class="language-python">raise</code></pre>

Пример:

<pre><code class="language-python">age = -5

if age < 0:
    raise ValueError("Возраст не может быть отрицательным")</code></pre>

Результат:

<pre><code>ValueError:
Возраст не может быть отрицательным</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 16. Практический пример</b>

Программа просит число до тех пор, пока пользователь не введёт его правильно.

<pre><code class="language-python">while True:
    try:
        number = int(input("Введите число: "))
        print("Спасибо!")
        break

    except ValueError:
        print("Нужно ввести число")</code></pre>

Пример использования:

<pre><code>Введите число: abc
Нужно ввести число

Введите число: hello
Нужно ввести число

Введите число: 15
Спасибо!</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 17. Типичные ошибки новичков</b>

<b>❌ Использование голого except</b>

Плохо:

<pre><code class="language-python">try:
    ...
except:
    print("Ошибка")</code></pre>

Так можно случайно скрыть серьёзные ошибки.

Лучше:

<pre><code class="language-python">except ValueError:</code></pre>

━━━━━━━━━━━

<b>❌ Пустой except</b>

Плохо:

<pre><code class="language-python">try:
    ...
except:
    pass</code></pre>

Ошибка будет скрыта.

Поиск проблем станет намного сложнее.

━━━━━━━━━━━

<b>❌ Слишком много кода внутри try</b>

Плохо:

<pre><code class="language-python">try:
    # 50 строк кода
    ...
except:
    ...</code></pre>

Чем меньше блок try — тем проще искать ошибку.

━━━━━━━━━━━

<b>❌ Использование исключений вместо условий</b>

Плохо:

<pre><code class="language-python">try:
    print(numbers[0])
except:
    ...</code></pre>

Иногда проще сначала проверить условие:

<pre><code class="language-python">if numbers:
    print(numbers[0])</code></pre>

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• исключение — это ошибка во время выполнения программы
• для обработки ошибок используется:

<pre><code class="language-python">try-except</code></pre>
• можно ловить конкретные типы ошибок
• самые частые ошибки:
  - ValueError
  - TypeError
  - ZeroDivisionError
  - IndexError
  - KeyError
  - FileNotFoundError
• else выполняется только если ошибки не было
• finally выполняется всегда
• raise позволяет создавать собственные исключения
• обработка исключений делает программы устойчивыми и удобными для пользователей