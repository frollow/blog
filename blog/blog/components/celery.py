from celery.schedules import crontab


CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

# celery_singleton
CELERY_SINGLETON_BACKEND_URL = "redis://localhost:6379/0"
CELERY_SINGLETON_LOCK_EXPIRY = 600  # seconds

CELERY_BEAT_SCHEDULE = {
    "fetch-and-create-post-twice-hourly": {
        "task": "posts.tasks.fetch_and_create_post",
        "schedule": crontab(minute="*/28"),  # каждые 28 минут
    },
}


CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
