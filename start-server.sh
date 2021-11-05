#!/usr/bin/env bash
# start-server.sh
echo "Hallo von Nabucco"
if [ -n "$MIGRATE" ] ; then
    (echo "making migrations and running them"
    python djangobaseproject/manage.py migrate --no-input)
fi
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (echo "creating superuser ${DJANGO_SUPERUSER_USERNAME}" && python djangobaseproject/manage.py createsuperuser --no-input --noinput --email 'blank@email.com')
fi
cd djangobaseproject && python manage.py collectstatic --no-input && gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"