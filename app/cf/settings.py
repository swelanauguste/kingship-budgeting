import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", default=0)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "crispy_forms",
    "crispy_bootstrap5",
    "pwa",
    "after_response",
    "users",
    "accounts",
    "incomes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "dev.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "prod.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/St_Lucia"

USE_I18N = True

USE_TZ = True

directories = [
    "templates",
    "static",
    "debug",
    "static/css",
    "static/images",
    "static/js",
    "static/icons",
]

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files (user-uploaded files)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Crispy forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Custom user model
AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "users.backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]
PASSWORD_RESET_TIMEOUT = 3600

SITE_ID = 1

# Redirect URLs
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/users/login/"
LOGOUT_URL = "/users/login/"

# Email settings
ADMINS = [
    ("kingship.lc", "kingship.lc@gmail.com"),
]


DEFAULT_FROM_EMAIL = "complaints.infrastructure@gmail.com"

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = "emails"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    # EMAIL_HOST = "mail.govt.lc"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "kingship.lc@gmail.com"
    EMAIL_HOST_PASSWORD = os.environ.get("PASS")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    # EMAIL_USE_SSL = False

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname}, {asctime}, {module}, {process:d}, {thread:d}, {message}",
                "style": "{",
            },
            "simple": {
                "format": "{levelname} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "file": {
                "level": "WARNING",
                "class": "logging.FileHandler",
                "filename": BASE_DIR / "debug/debug.log",
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file", "mail_admins"],
                "level": "WARNING",
                "propagate": True,
            },
        },
    }
    
# PWA settings
PWA_APP_NAME = "Expenses"
PWA_APP_DESCRIPTION = "Expenses tracker"
PWA_APP_THEME_COLOR = "#0A0302"
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [{"src": "/static/images/logo.png", "sizes": "160x160"}]
PWA_APP_ICONS_APPLE = [{"src": "/static/images/logo.png", "sizes": "160x160"}]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/images/logo.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"
PWA_APP_SHORTCUTS = [
    {
        "name": "Shortcut",
        "url": "/target",
        "description": "Shortcut to a page in my application",
    }
]
PWA_APP_SCREENSHOTS = [
    {
        "src": "/static/images/icons/splash-750x1334.png",
        "sizes": "750x1334",
        "type": "image/png",
    }
]