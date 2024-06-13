#!/bin/sh


echo "Applying database migrations..."
python manage.py migrate --noinput


echo "Starting server..."
exec gunicorn --workers=3 kestsikz.wsgi:application --bind 0.0.0.0:8001