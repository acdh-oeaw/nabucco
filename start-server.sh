#!/usr/bin/env bash
# start-server.sh
echo "Hello from Project Nabucco"
python manage.py collectstatic --no-input
echo "running migrations"
python manage.py migrate --no-input
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (echo "creating superuser ${DJANGO_SUPERUSER_USERNAME}" && python manage.py createsuperuser --no-input --noinput --email 'blank@email.com')
fi
gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"