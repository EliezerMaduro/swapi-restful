import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'technical_challenge_ntd.settings')

app = Celery('technical_challenge_ntd')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()