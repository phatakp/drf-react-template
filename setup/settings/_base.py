"""
Django Common settings for project.
"""

import sys
from datetime import timedelta
from os import getenv
from os.path import basename, join, normpath
from pathlib import Path

from dotenv import load_dotenv

# =========PATH CONFIGURATION =======================

# Django Project Setup Directory
SETTINGS_ROOT = Path(__file__).resolve().parent.parent

# Project Root Folder
PROJECT_ROOT = SETTINGS_ROOT.parent

# Name of the whole site
SITE_NAME = basename(SETTINGS_ROOT)


# STATIC Files in dev
STATICFILES_DIRS = [PROJECT_ROOT / "staticfiles"]

# Template Directory
TEMPLATE_DIR = [PROJECT_ROOT / "templates"]


# add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, "apis")))

load_dotenv(join(PROJECT_ROOT, ".env"))


# ==================== APPLICATION CONFIG =========================

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt.token_blacklist",
    "drf_standardized_errors",
]

LOCAL_APPS = [
    "apis.users.apps.UsersConfig",
]

AUTH_USER_MODEL = "users.User"

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


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
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


# Database
DATABASES = {}


# Password validation
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# the default WSGI application
WSGI_APPLICATION = f"{SITE_NAME}.wsgi.application"


# the root URL configuration
ROOT_URLCONF = f"{SITE_NAME}.urls"

# Django config
SECRET_KEY = str(getenv("SECRET_KEY"))
DEBUG = str(getenv("DEBUG")) == "True"
ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = PROJECT_ROOT / "static"
MEDIA_URL = "media/"
STATIC_ROOT = PROJECT_ROOT / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django CORS
CORS_ALLOW_CREDENTIALS = True

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "drf_standardized_errors.exception_handler",
}
DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

# JWT Settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

JWT_COOKIE_NAME = getenv("JWT_COOKIE_NAME")
JWT_COOKIE_SAMESITE = getenv("JWT_COOKIE_SAMESITE")
JWT_COOKIE_SECURE = getenv("JWT_COOKIE_SECURE") == "True"
