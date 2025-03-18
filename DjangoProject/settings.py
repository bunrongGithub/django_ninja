import os
DJANGO_ENV = os.environ.get("DJANGO_ENV", "development")
if DJANGO_ENV == 'production':
    from settings.production import *
else:
    from settings.development import *