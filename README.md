# Парсер вакансий с hh.ru
Этот проект позволяет получать информацию о компаниях и вакансиях с сайта HH.ru.

## Установка
1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/ArkadiyGenij/course_work_5.git
    ```
2. Перейдите в директорию проекта:

    ```bash
    cd course_work_5
    ```

3. Установите зависимости:

    ```bash
    poetry install
    ```

## Использование

1. Запустите программу:

    ```bash
    poetry run python main.py
    ```
2. Программа получит данные о компаниях с сайта HH.ru и выведет информацию о вакансиях этих компаний. Далее с помощью интуитивно понятного меню вы сможете пользоваться программой.

## Настройка

Для работы программы необходимо настроить доступ к базе данных PostgreSQL. Создайте файл `database.ini` в корне проекта и добавьте следующие настройки:

```ini
[postgresql]
host=localhost
database=your_database
user=your_username
password=your_password
port=5432
