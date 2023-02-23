# Тестовое задание веб-программист (Python)

Нужно разработать Telegram бота, который при старте запросит номер телефона клиента, отправит запрос на приемщик и отпишется клиенту в боте об успехе

Подробное описание:
```
1. Зарегистрировать нового бота через BotFather [https://t.me/botfather](https://t.me/botfather)
2. Развернуть Django глобально
3. 1 раз установить webhook url, можно через postman [https://core.telegram.org/bots/api#setwebhook](https://core.telegram.org/bots/api#setwebhook)
4. Когда добавляем бота, отображается Start, при клике на webhook уходит соответствующий запрос, если это именно первый Start, то отправляем через [https://core.telegram.org/bots/api#sendmessage](https://core.telegram.org/bots/api#sendmessage) сообщение “Привет, а дай номер”. Через reply_markup добавляем кнопку с параметром request_contact, чтобы при клике на нее отправлялся номер клиента на webhook
5. Если нам приходит номер(клик по кнопке пункта 4), то отправляем его POST запросом на [https://s1-nova.ru/app/private_test_python/](https://s1-nova.ru/app/private_test_python/) с данными в формате JSON(content-type заголовок обязателен) 
```
```
{”phone”:”номер телефона”,”login”:”Логин в телеграме”}
```

На приемщике есть логирование
[https://s1-nova.ru/app/private_test_python/log.log](https://s1-nova.ru/app/private_test_python/log.log)

Нужно использовать:

- Фреймворк Django

Запуск проекта
1. Скронируйте репозиторий на локальную машину:
```
git@github.com:Linnaip/Nova_cv.git
```
2. Создайте .env файл в директории /, в котором должны содержаться следующие переменные для подключения:
```
TELEGRAM_TOKEN = 'Ваш телеграм токен'
```
3. Выполните команду:
```
sudo docker run -d linnaip/nova_cv:version0.1
```
```
В Windows команда выполняется без sudo
```

### Проект развернут при помощи cloud.yandex.

### Автор
```
Лычагин Андрей (Github - Linnaip)
```