#!/bin/bash
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

gunicorn QRGenProject.wsgi
