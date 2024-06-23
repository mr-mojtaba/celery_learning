from celery import Celery


app = Celery('core')

app.config.from_object('django.conf:settings', namespace='CELERY')
