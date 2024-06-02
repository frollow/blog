from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.signals import worker_ready
from celery_singleton import clear_locks

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

app = Celery("blog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@worker_ready.connect
def unlock_all(**kwargs):
    clear_locks(app)
