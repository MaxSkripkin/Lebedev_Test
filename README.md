# Cервис для популяризации открытых данных в России.

Проект парсит таблицу в формате csv в PostrgreSQL. Содержимое базы данных доступно для всех по API. Реализован поиск по данным.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

### Проект доступен по адресу http://158.160.1.235/api/v1/

### Документация доступна по адресам http://158.160.1.235/swagger/   http://158.160.1.235/redoc/

### Главная страница

Содержит указы президента, нажимая на фильтры можно применить поиск по названию указа. 

# Подготовка к запуску и запуск проекта

В папке infra создать файл .env и наполнить его следующим содержимым:

    ```
 DB_ENGINE=django.db.backends.postgresql
 DB_NAME=postgres
 POSTGRE_USER=postgres
 POSTGRES_PASSWORD=postgres
 DB_HOST=db
 DB_PORT=5432
    ```

Зайти в консоль bash, перейти в папку infra и выполнить команды:

winpty docker-compose up -d

winpty docker-compose exec web python manage.py makemigrations

winpty docker-compose exec web python manage.py migrate

winpty docker-compose exec web python manage.py import_csv

winpty docker-compose exec web python manage.py collectstatic --no-input
