#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn QRGenProject.wsgi:application
