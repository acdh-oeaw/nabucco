#!/usr/bin/env bash
echo "Hello from Project nabucco"
uv run manage.py collectstatic --no-input
echo "running migrations"
uv run manage.py migrate --no-input
uv uv run manage.py prune_no_author_logs  
uv run gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"