import os

from django.conf import settings

BASE_DIR = settings.BASE_DIR

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
if settings.DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
else:
    MEDIA_ROOT = "/var/www/media/"
    STATIC_ROOT = "/var/www/static/"
    STATIC_ROOT = "/var/www/static/"
