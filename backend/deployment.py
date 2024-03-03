import os
from settings import *
from settings import BASE_DIR


ALLOWED_HOSTS = [os.environ["website"]]
SRF_TRUSTED_ORIGINS = ["https://"+os.environ["website"]]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

CORS_ALLOWED_ORIGINS = [

]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNENCTION_STR = {pair.split("=")[0]:pair.split("=")[1] for pair in CONNECTION.split(" ")}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNENCTION_STR['dbname'],
        "USER": CONNENCTION_STR['user'],
        "PASSWORD": CONNENCTION_STR["password"],
        "HOST": CONNENCTION_STR['host']
    }
}

STATIC_ROOT = BASE_DIR/"staticfiles"