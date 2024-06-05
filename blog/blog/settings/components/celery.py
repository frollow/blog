import os
from celery.schedules import crontab

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_WORKER_POOL = "solo"

# celery_singleton
CELERY_SINGLETON_BACKEND_URL = os.environ.get('CELERY_SINGLETON_BACKEND_URL')
CELERY_SINGLETON_LOCK_EXPIRY = 600  # seconds

CELERY_BEAT_SCHEDULE = {
    "fetch-and-create-post-twice-hourly": {
        "task": "posts.tasks.fetch_and_create_post",
        "schedule": crontab(minute="*/28"),  # каждые 28 минут
    },
}

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True