import requests
from bs4 import BeautifulSoup

# Получаем ссылку на поссылку
# Для тестов: https://litemf.com/ru/tracking?tracking_number=LP2056555
url = input("Enter the link to the parcel: ")

# Код новой страницы
start_page = """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="apple-itunes-app" content="app-id=1484449544">
    <meta name="google-play-app" content="app-id=com.litemf">
            <meta name="description" content="Хотите узнать как отследить посылку? Отслеживание посылок и заказов из интернет-магазинов на нашем сайте.">
                <meta name="keywords" content="отследить посылку, отслеживание посылок, как отследить посылку">
    
    <title>LiteMF — Как отследить посылку: отслеживание заказов</title>

            <link rel="alternate" hreflang="ru" href="https://litemf.com/ru/tracking">
            <link rel="alternate" hreflang="en" href="https://litemf.com/en/tracking">
        <link rel="canonical" href="https://litemf.com/ru/tracking">

    <link href="frontend.d1aa8bad.css" rel="stylesheet">
    <script defer id="script" src="/build/frontend.d1aa8bad.js"></script>
    </head>
    <body>
"""

end_page = """
    </body>
</html>
"""

# Получаем контент со страницы
req = requests.get(url)
content = req.text

# Ищем нужный контент по тегам
soup = BeautifulSoup(content, 'lxml')
page = soup.find('div', class_='layout-page')

# "Собираем" новую страницу
new_page = start_page + page.prettify() + end_page

# Сохраним в html файл
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(new_page)
