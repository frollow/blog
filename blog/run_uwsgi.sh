#!/usr/bin/env bash

set -e

chown www-data:www-data /var/log

python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py compilemessages -l en -l ru

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL" || true
fi

uwsgi --strict --ini /opt/app/uwsgi.ini
