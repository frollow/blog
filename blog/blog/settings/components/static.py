import os

from django.conf import settings

BASE_DIR = settings.BASE_DIR

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"

MEDIA_ROOT = "/var/www/media/"
STATIC_ROOT = "/var/www/static/"
