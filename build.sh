#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve
python3 manage.py runserver "0.0.0.0:8000"