#!/bin/bash -x

python3 ./serv/manage.py makemigrations && python3 ./serv/manage.py migrate && ./serv/manage.py collectstatic --no-input && gunicorn --chdir serv --bind 0.0.0.0:8000 config.wsgi:application
#&& python3 ./serv/manage.py runserver 0.0.0.0:8000
#&& gunicorn --chdir serv --bind 0.0.0.0:8000 config.wsgi:application
