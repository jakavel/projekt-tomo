#!/bin/sh

./manage.py migrate --no-input
./manage.py collectstatic --no-input
uwsgi
