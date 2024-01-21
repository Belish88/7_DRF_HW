# 7_DRF_HW

Запуск проекта

Для запуска проекта должен быть установлен docker engine. Инструкция по установке: https://docs.docker.com/engine/install/
Для Ubuntu, дополнительно нужно установить docker-compose:

sudo apt install docker-compose

В корне проекта необходимо создать и заполнить файл .env:

# .env

DEBUG='on'

SECRET_KEY=

DATABASE_NAME=

DATABASE_USER=

DATABASE_PASSWORD=

DATABASE_HOST='db'

STRIPE_API_KEY=

EMAIL_HOST_USER=

EMAIL_HOST_PASSWORD=

Для первого запуска необходимо собрать образ контейнера. Для этого, находясь в корневой директории проекта необходимо выполнить команду:

sudo docker-compose build

Для запуска проекта:

sudo docker-compose up

Веб приложение будет доступно по адресу: http://127.0.0.1:8000

Cоздание admina:

docker-compose exec app python3 manage.py csu 

Администратор:

email = 'admin@sky.pro'

password = '5080'
