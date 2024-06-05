import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
