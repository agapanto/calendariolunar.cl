release: python manage.py migrate
web: gunicorn -b 0.0.0.0:${PORT} -w 8 -t 90 calendariolunar.wsgi --log-file -
