#!/bin/sh

poetry run python3 /service/manage.py migrate --noinput
poetry run python3 /service/manage.py runserver 0.0.0.0:8000

exec "$@"