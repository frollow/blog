import os

from django.conf import settings
from dotenv import load_dotenv
from storages.backends.s3boto3 import S3Boto3Storage

load_dotenv()


BASE_DIR = settings.BASE_DIR

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# AWS settings based on digital ocean S3
# https://www.digitalocean.com/community/tutorials/how-to-set-up-object-storage-with-django
AWS_STATIC_LOCATION = "static"
AWS_PUBLIC_MEDIA_LOCATION = "media"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")


class MediaStorage(S3Boto3Storage):
    file_overwrite = False
    location = AWS_PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    gzip = True

    def get_object_parameters(self, name):
        s3_object_params = {
            "CacheControl": "public, max-age=2592000",
        }
        return {**s3_object_params}


class StaticStorage(S3Boto3Storage):
    file_overwrite = False
    location = AWS_STATIC_LOCATION
    default_acl = "public-read"
    gzip = True

    def get_object_parameters(self, name):
        s3_object_params = {
            "CacheControl": "public, max-age=86400",
        }
        return {**s3_object_params}


STATIC_URL = "dd/"  # Doesn't matter. Empty static prefix not permitted.

STORAGES = {
    "default": {
        "BACKEND": "blog.settings.components.static.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "blog.settings.components.static.StaticStorage",
    },
}

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # other finders..
    "compressor.finders.CompressorFinder",
)


COMPRESS_OUTPUT_DIR = "cache"
