#!/bin/bash
/etc/init.d/cron start
cd /src/teonitesp
python3 manage.py migrate
python3 scraper.py
echo Starting Gunicorn.
exec gunicorn teonitesp.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3
