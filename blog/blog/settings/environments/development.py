import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

# common.py
DEBUG = True

INSTALLED_APPS = settings.INSTALLED_APPS
MIDDLEWARE = settings.MIDDLEWARE
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# static.py
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")