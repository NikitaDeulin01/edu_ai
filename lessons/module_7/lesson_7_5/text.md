<b>🌐 Урок 7.5. Введение в парсинг сайтов</b>

<i>Интернет содержит огромное количество данных: новости, цены товаров, вакансии, курсы валют, расписания и многое другое. Иногда эти данные нужно получать автоматически. Для этого используется парсинг.</i>

━━━━━━━━━━━
<b>ЧАСТЬ 1. Что такое парсинг</b>

<b>Парсинг</b> — это автоматическое получение и извлечение данных из веб-страниц.

Например:

• собрать цены товаров

• получить список вакансий

• скачать новости

• собрать курсы валют

• получить расписание рейсов

━━━━━━━━━━━

Без парсинга человеку пришлось бы копировать информацию вручную.

━━━━━━━━━━━
<b>ЧАСТЬ 2. Как работает сайт</b>

Когда вы открываете сайт:

<pre><code>https://example.com</code></pre>

браузер отправляет запрос серверу.

Сервер отвечает страницей.

Чаще всего это:

<pre><code>HTML</code></pre>

документ.

━━━━━━━━━━━

Схема выглядит так:

<pre><code>Браузер
   ↓
HTTP-запрос
   ↓
Сервер
   ↓
HTML-страница
   ↓
Браузер показывает сайт</code></pre>

Парсер делает почти то же самое.

━━━━━━━━━━━
<b>ЧАСТЬ 3. Что такое HTML</b>

HTML — язык разметки веб-страниц.

Пример:

<pre><code class="language-html">&lt;h1&gt;Мой сайт&lt;/h1&gt;

&lt;p&gt;Текст страницы&lt;/p&gt;</code></pre>

Здесь:

<pre><code class="language-html">&lt;h1&gt;</code></pre>

заголовок.

━━━━━━━━━━━

<pre><code class="language-html">&lt;p&gt;</code></pre>

абзац текста.

━━━━━━━━━━━

Большинство парсеров работают именно с HTML.

━━━━━━━━━━━
<b>ЧАСТЬ 4. Библиотека requests</b>

Для получения страницы используется библиотека:

<pre><code>requests</code></pre>

Установка:

<pre><code class="language-bash">pip install requests</code></pre>

Импорт:

<pre><code class="language-python">import requests</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 5. Первый запрос</b>

Пример:

<pre><code class="language-python">import requests

response = requests.get(
    "https://example.com"
)

print(response.text)</code></pre>

Результат:

Будет выведен HTML страницы.

━━━━━━━━━━━

Метод:

<pre><code class="language-python">requests.get()</code></pre>

отправляет GET-запрос.

━━━━━━━━━━━
<b>ЧАСТЬ 6. Статус-коды ответа</b>

Каждый сервер отвечает специальным кодом.

Получить код:

<pre><code class="language-python">print(response.status_code)</code></pre>

━━━━━━━━━━━

Самые популярные:

<table>
<tr>
<td><b>Код</b></td>
<td><b>Значение</b></td>
</tr>

<tr>
<td>200</td>
<td>Успех</td>
</tr>

<tr>
<td>404</td>
<td>Страница не найдена</td>
</tr>

<tr>
<td>403</td>
<td>Доступ запрещён</td>
</tr>

<tr>
<td>500</td>
<td>Ошибка сервера</td>
</tr>
</table>

━━━━━━━━━━━
<b>ЧАСТЬ 7. Проверка успешного запроса</b>

Обычно делают так:

<pre><code class="language-python">if response.status_code == 200:
    print("Успешно")
else:
    print("Ошибка")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 8. Что такое BeautifulSoup</b>

Получить HTML недостаточно.

Нужно ещё извлечь данные.

Для этого используют библиотеку:

<pre><code>BeautifulSoup</code></pre>

Установка:

<pre><code class="language-bash">pip install beautifulsoup4</code></pre>

Импорт:

<pre><code class="language-python">from bs4 import BeautifulSoup</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 9. Создание объекта BeautifulSoup</b>

Пример:

<pre><code class="language-python">from bs4 import BeautifulSoup

html = """
&lt;h1&gt;Python&lt;/h1&gt;
"""

soup = BeautifulSoup(
    html,
    "html.parser"
)</code></pre>

Теперь объект:

<pre><code class="language-python">soup</code></pre>

умеет искать элементы страницы.

━━━━━━━━━━━
<b>ЧАСТЬ 10. Получение первого элемента</b>

Пример:

<pre><code class="language-python">print(soup.h1)</code></pre>

Результат:

<pre><code>&lt;h1&gt;Python&lt;/h1&gt;</code></pre>

━━━━━━━━━━━

Получить текст:

<pre><code class="language-python">print(soup.h1.text)</code></pre>

Результат:

<pre><code>Python</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 11. Метод find()</b>

Позволяет найти первый элемент.

Пример:

<pre><code class="language-python">title = soup.find("h1")

print(title.text)</code></pre>

━━━━━━━━━━━

Найти абзац:

<pre><code class="language-python">soup.find("p")</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 12. Метод find_all()</b>

Получить все элементы.

Пример:

<pre><code class="language-python">html = """
&lt;li&gt;Python&lt;/li&gt;
&lt;li&gt;Java&lt;/li&gt;
&lt;li&gt;Go&lt;/li&gt;
"""

soup = BeautifulSoup(
    html,
    "html.parser"
)

items = soup.find_all("li")

for item in items:
    print(item.text)</code></pre>

Результат:

<pre><code>Python
Java
Go</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 13. Работа с атрибутами</b>

HTML:

<pre><code class="language-html">&lt;a href="https://python.org"&gt;
Python
&lt;/a&gt;</code></pre>

Получение ссылки:

<pre><code class="language-python">link = soup.find("a")

print(link["href"])</code></pre>

Результат:

<pre><code>https://python.org</code></pre>

━━━━━━━━━━━
<b>ЧАСТЬ 14. Парсинг реального сайта</b>

Пример:

<pre><code class="language-python">import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://example.com"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

title = soup.find("h1")

print(title.text)</code></pre>

━━━━━━━━━━━

Получаем страницу и извлекаем заголовок.

━━━━━━━━━━━
<b>ЧАСТЬ 15. User-Agent</b>

Некоторые сайты блокируют парсеров.

Тогда отправляют заголовки.

Пример:

<pre><code class="language-python">headers = {
    "User-Agent":
    "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)</code></pre>

Так запрос выглядит как обычный браузер.

━━━━━━━━━━━
<b>ЧАСТЬ 16. Сохранение данных</b>

Полученные данные можно сохранять.

Например:

<pre><code class="language-python">with open(
    "titles.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(title)</code></pre>

━━━━━━━━━━━

Или сохранять в CSV.

━━━━━━━━━━━
<b>ЧАСТЬ 17. Ограничения парсинга</b>

Не все сайты разрешают парсинг.

Некоторые:

• требуют авторизацию

• используют защиту от ботов

• ограничивают количество запросов

• показывают данные через JavaScript

━━━━━━━━━━━

Поэтому парсер не всегда работает "из коробки".

━━━━━━━━━━━
<b>ЧАСТЬ 18. Когда лучше использовать API</b>

Если сайт предоставляет API —

используйте API.

Это:
✅ быстрее
✅ стабильнее
✅ надёжнее
✅ официально поддерживается

━━━━━━━━━━━

Например:

GitHub API

Telegram API

OpenWeather API

OpenAI API

━━━━━━━━━━━
<b>ЧАСТЬ 19. Где используется парсинг</b>
📈 Мониторинг цен
📰 Сбор новостей
💼 Сбор вакансий
📊 Аналитика рынка
🤖 Telegram-боты
🛒 Интернет-магазины
📉 Финансовые данные
🧠 Data Science

━━━━━━━━━━━
<b>ЧАСТЬ 20. Типичные ошибки новичков</b>

<b>❌ Забывают установить библиотеку</b>

Ошибка:

<pre><code>ModuleNotFoundError</code></pre>

Решение:

<pre><code class="language-bash">pip install requests
pip install beautifulsoup4</code></pre>

━━━━━━━━━━━

<b>❌ Не проверяют status_code</b>

Неправильно:

<pre><code class="language-python">response = requests.get(url)

print(response.text)</code></pre>

Лучше:

<pre><code class="language-python">if response.status_code == 200:
    print(response.text)</code></pre>

━━━━━━━━━━━

<b>❌ Путают find() и find_all()</b>

<pre><code class="language-python">find()</code></pre>

возвращает один элемент.

━━━━━━━━━━━

<pre><code class="language-python">find_all()</code></pre>

возвращает список элементов.

━━━━━━━━━━━

<b>❌ Пытаются парсить сайт без изучения HTML</b>

Перед написанием парсера нужно посмотреть структуру страницы через инструменты разработчика браузера.

━━━━━━━━━━━
<b>ЧТО ВАЖНО ЗАПОМНИТЬ</b>
• парсинг — автоматическое получение данных с сайтов
• requests используется для отправки HTTP-запросов
• BeautifulSoup помогает извлекать данные из HTML
• response.text содержит HTML страницы
• status_code показывает результат запроса
• find() ищет один элемент
• find_all() ищет несколько элементов
• через атрибуты можно получать ссылки и другие данные
• многие сайты ограничивают парсинг
• если есть API — обычно лучше использовать его