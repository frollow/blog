"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings

Default environment is `developement`.

To change settings file:

`DJANGO_ENV=production python manage.py runserver`

"""

from os import environ

from split_settings.tools import include, optional

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "components/common.py",  # standard django settings
    "components/database.py",
    "components/thumbnail.py",
    "components/templates.py",
    "components/internationalization.py",
    "components/static.py",
    "components/caches.py",
    "components/logging.py",
    "components/celery.py",
    "components/email.py",
    "components/ckeditor.py",
    "components/sanitizer.py",

    # Select the right env:
    "environments/%s.py" % ENV,

    # Optionally override some settings:
    optional("environments/local.py"),
]

# Include settings:
include(*base_settings)
