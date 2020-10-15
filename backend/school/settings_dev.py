from pathlib import Path  # python3 only

from dotenv import load_dotenv

from .settings_base import *

env_path = f'{BASE_DIR}/environment.env'

load_dotenv(dotenv_path=env_path)

SECRET_KEY = "paul"

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'onteri-school.herokuapp.com', '*.herokuapp', '*']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 60 * 24

# cacheops
CACHEOPS_REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 1,
    'socket_timeout': 3,
}

CACHEOPS_DEGRADE_ON_FAILURE = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['../frontend/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'



# cache feedback
def stats_collector(sender, func, hit, **kwargs):
    event = 'hit' if hit else 'miss'
    print(event)
    print(func)


from cacheops.signals import cache_read

cache_read.connect(stats_collector)
