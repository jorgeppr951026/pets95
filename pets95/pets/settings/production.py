from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd23to9736v19jn',
        'USER':'grwpacnijsfpkl',
        'PASSWORD':'3d4cfea2dd19052f72fe6987f080a7fec434133c69aa3cdb0bafdb3cc9ec59e9',
        'HOST':'ec2-3-95-130-249.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')