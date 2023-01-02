#!/bin/bash
python manage.py makemigrations
python manage.py migrate

gunicorn QRGenProject.wsgi:application
