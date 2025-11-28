from celery import Celery
from app.config import settings

celery = Celery(
    "agrisure",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery.conf.task_serializer = 'json'
celery.conf.result_serializer = 'json'
celery.conf.accept_content = ['json']
