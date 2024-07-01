#!/bin/bash

python manage.py migrate --noinput

waitress-serve --port=$PORT tstprdstageapp1_de_136064.wsgi:application
