from django.conf import settings


INSTALLED_APPS = settings.INSTALLED_APPS
MIDDLEWARE = settings.MIDDLEWARE

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")