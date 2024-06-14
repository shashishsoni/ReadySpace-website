import os
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-03bg9=(58icn)nh$ug1jf!_^(ag^(5ng=$%^h#z(cafo_nv-=$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


#try:
 #   from .local import *
#except ImportError:
#   pass
