import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kestesikz.settings')
app = Celery('kestesikz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update_instagram_posts_every_4_hours': {
        'task': 'instagram_parsing.tasks.update_instagram_posts_task',
        'schedule': crontab(minute=0, hour='*/4'),
    },
}