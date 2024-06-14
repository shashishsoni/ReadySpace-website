from .base import *
import os

DEBUG = False
SECRET_KEY = '5=#ur&ckks6^0pa5s3admpj)ed=8f*(f!seymn#*@ycis_lyxw'
ALLOWED_HOSTS = ['localhost', 'SpaceReady.com', '*']


cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND":
            "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'djongo.db.backends.postgresql_psycopg2',
        "NAME": 'SpaceReady',
        "USER": 'SpaceReady',
        "PASSWORD": 'Shashish@#$7321',
        "HOST": 'localhost',
        "PORT": "",
    }
}

# settings.py
import sentry_sdk

sentry_sdk.init(
    dsn="https://083e84c80e9e08029cb024acdb87ff18@o4506605237305344.ingest.sentry.io/4506605241106432",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
