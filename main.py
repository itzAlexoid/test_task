# 1. Задача: В офисе есть 5 кабинетов. Не используя фреймворки,
# написать команду, которая проверяет свободен ли кабинет
# в определенное время и даст возможность его забронировать.
# После бронирования кабинета, чтоб была команда — Отправлять
# уведомление человеку, который занимает его
# (на Email и номер телефона) с датой, временем и номером
# кабинета. Если кабинет занят, выводить сообщение кем и до
# скольки он занят. Использовать СУБД.
#
# Желательно использовать PEP-стандарты. Во время разработки
# используйте git и Github и делайте значимые коммиты.
# Результаты задачи должны быть размещены в вашей учетной
# записи Github, отправьте нам только ссылку. Мы не принимаем
# результаты задач в .zip/.rar и т. д.


import psycopg2
from datetime import datetime

# Коннект с базой данных

conn = psycopg2.connect(
        dbname="",
        user="",
        password="",
        host="localhost",
	port="5000"
)
return conn

