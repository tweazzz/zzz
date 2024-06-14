from .services import *
from celery import shared_task

@shared_task
def update_instagram_posts_task():
    update_instagram_posts()