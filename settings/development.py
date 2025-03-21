from .base import *

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DEV_POSTGRESQL_DATABASE"),
        "USER": env("DEV_POSTGRESQL_USER"),
        "PASSWORD": env("DEV_POSTGRESQL_PASSWORD"),
        "HOST": env("DEV_POSTGRESQL_HOST"),
        "PORT": env("DEV_POSTGRESQL_PORT"),
    }
}
