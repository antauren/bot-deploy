# Телеграмм-бот Devman на Heroku

1. Телеграмм-бот информирует о проверке работ в Devman 
2. Код предназначен для запуска на сервере Heroku

## Чтобы запустить, потребуются следующие данные

* `token_devman` - токен ученика Devman
* `token_telegram_bot` - токен телеграмм-бота, который отправит уведомление
* `chat_id_telegram` - id телеграмм-чата, который получит уведомление

### Как запустить на Heroku

1. Зарегестрируйте приложение на [Heroku]
2. В созданном приложении во вкладке `Deploy`
привяжите данный github-репозиторий в `Deployment method`
и нажмите `Deploy Branch` внизу страницы
3. Во вкладке `Settings` заполните переменные `Config Vars`: `token_devman`, `token_telegram_bot`, `chat_id_telegram`
4. Во вкладке `Resources` запустите сервер


### Как запустить на своей машине

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

1. Создайте в корневой папке файл ```.env``` и пропишите в нем переменные следующим образом:  
    ```
    token_devman=Token 123abc456abc
    chat_id_telegram=75845
    token_telegram_bot=123456:fdg7gf234dgFH65
    ```

2. Запустите ```python devman_bot_dev.py```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

[Heroku]: https://id.heroku.com/login "Heroku"