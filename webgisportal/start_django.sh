#!/bin/bash
echo 'django migrate'
python manage.py migrate
echo 'django runserver'
gunicorn --bind :8080 --workers 3 "webgisportal.wsgi:application"