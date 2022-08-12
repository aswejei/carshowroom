#!/bin/bash -x

python3 ./serv/manage.py makemigrations
python3 ./serv/manage.py migrate
python3 ./serv/manage.py runserver 0.0.0.0:8000
