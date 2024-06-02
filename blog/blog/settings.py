import os

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True") == "True"

allowed_hosts_env = os.getenv("ALLOWED_HOSTS", "127.0.0.1")
internal_hosts_env = os.getenv("INTERNAL_IPS", "127.0.0.1")
ALLOWED_HOSTS = allowed_hosts_env.split(",")
INTERNAL_IPS = internal_hosts_env.split(",")

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
]
CSRF_FAILURE_VIEW = "core.views.csrf_failure"

ROOT_URLCONF = "blog.urls"
WSGI_APPLICATION = "blog.wsgi.application"

# Fixed parameters
POSTS_FOR_PAGINATION = 10
THUMBNAIL_FORMAT = "WEBP"

INSTALLED_APPS = [
    "sorl.thumbnail",
    "homepage.apps.HomepageConfig",
    "posts.apps.PostsConfig",
    "users.apps.UsersConfig",
    "core.apps.CoreConfig",
    "contacts.apps.ContactsConfig",
    "social.apps.SocialConfig",
    "search.apps.SearchConfig",
    "links.apps.LinksConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_recaptcha",
    "django_json_ld",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Login
LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "posts:index"
# LOGOUT_REDIRECT_URL = 'posts:index'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

include(
    "components/database.py",
    "components/templates.py",
    "components/internationalization.py",
    "components/static.py",
    "components/logging.py",
    "components/celery.py",
    "components/email.py",
)
