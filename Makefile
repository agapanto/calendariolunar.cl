ifndef PORT
override PORT = 5000
endif

serve:
	python manage.py migrate
	gunicorn -b 0.0.0.0:${PORT} -w 8 -t 90 calendariolunar.wsgi --log-file -