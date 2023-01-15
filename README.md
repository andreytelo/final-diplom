## Установка

Склонируйте репозиторий с помощью git

    git clone https://github.com/andreytelo/final-diplom.git
Перейти в папку:
```bash
cd python-final-diplom
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
Перейти в папку с manage.py:
```bash
cd orders
```
# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```

* Команда для запуска приложения
```bash
python manage.py runserver
```