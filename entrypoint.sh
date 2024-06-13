#!/bin/sh


echo "Applying database migrations..."
python manage.py migrate --noinput


echo "Starting server..."
exec gunicorn kestsikz.wsgi:application --bind 0.0.0.0:8000