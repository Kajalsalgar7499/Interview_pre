from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "change-this-to-a-random-secret-key"

DEBUG = True

ALLOWED_HOSTS = []

# -------------------------
# Installed Apps
# -------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "users",
]

# -------------------------
# Middleware
# -------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "interview_platform.urls"

# -------------------------
# Templates
# -------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "interview_platform.wsgi.application"

# -------------------------
# Database
# -------------------------
# MongoDB is connected using pymongo in database/mongodb.py

DATABASES = {}

# -------------------------
# Password Validation
# -------------------------

AUTH_PASSWORD_VALIDATORS = []

# -------------------------
# Internationalization
# -------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# -------------------------
# Static Files
# -------------------------

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# -------------------------
# Media Files
# -------------------------

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"

# -------------------------
# Default Primary Key
# -------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"