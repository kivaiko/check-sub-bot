# check-sub-bot

![Static Badge](https://img.shields.io/badge/%D0%9F%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C_%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8E_%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC_%D0%B1%D0%BE%D1%82%D0%B0-blue?link=https%3A%2F%2Ft.me%2Feasyoffer_bot)


**check-sub-bot** – telegram бот, который проверяет наличие подписок
на несколько каналов и выдает ссылку на доступ к сайту [easyoffer.ru](http://easyoffer.ru)

В файле groups.py указываются телеграм каналы, они разделены главной и второчиной тематикой,
чтобы проверять подписку таргетированно. Для тех, кто интересуется Python, проверяется подписка на каналы по Python,
а для кто интересуется QA каналы по QA и т.д. и т.п.

## Установка

Склонируйте репозиторий
```
git clone https://github.com/kivaiko/check-sub-bot.git
```
Перейдите в папку с проектом
```
cd check-sub-bot
```
Создайте и запустите виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
Загрузите зависимости
```
pip install -r requirements.txt
```
Создайте своего телеграм бота через BotFather и получите токен

Создайте в папке проекта файл .env и пропишите в нем токен как в .env.example

Не забудьте добавить телеграм бота в качестве админа в свои каналы (они обязательно должны быть публичными)

В файле groups.py пропишите телеграм каналы

Запустите бота
```
python main.py
```



