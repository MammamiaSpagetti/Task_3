# Задание 3: UI-тесты Stellar Burgers

Проект содержит UI-тесты веб-приложения Stellar Burgers с Page Object Model,
фабрикой WebDriver для Chrome и Firefox и Allure-разметкой.

Тестовые пользователи создаются через API перед тестом и удаляются после него.

## Установка зависимостей

```shell
python -m pip install -r requirements.txt
```

## Запуск в Chrome и Firefox

```shell
python -m pytest tests --browser all --alluredir=allure-results --clean-alluredir
```

Запуск только в одном браузере:

```shell
python -m pytest tests --browser chrome
python -m pytest tests --browser firefox
```

Чтобы видеть окна браузеров, добавь параметр `--headed`.

## Создание и просмотр Allure-отчёта

```shell
allure generate allure-results -o allure-report --clean
allure open allure-report
```
