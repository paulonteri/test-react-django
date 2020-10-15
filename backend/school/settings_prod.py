from google.oauth2 import service_account

from .settings_base import *

# from pathlib import Path  # python3 only
# from dotenv import load_dotenv

# env_path = f'{BASE_DIR}/.env'
# load_dotenv(dotenv_path=env_path)

##

# TODO: Add timezone
SECRET_KEY = get_env_variable("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['api.demo.shulesuite.com',  'localhost']

CORS_ORIGIN_WHITELIST = ['https://demo.shulesuite.com',
                         'https://schoolonteri.netlify.app',
                         'http://localhost:3000',
                         'http://localhost:3001']

# Database
DATABASES = {
    'default': {
        'ENGINE': get_env_variable("DB_ENGINE"),
        'NAME': get_env_variable("DB_NAME"),
        'USER': get_env_variable("DB_USER"),
        'PASSWORD': get_env_variable("DB_PASSWORD"),
        'HOST': get_env_variable("DB_HOST"),
        'PORT': get_env_variable("DB_PORT"),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./frontend/templates'],
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

# Cache
CACHES = {
    "default": {
        "BACKEND": get_env_variable("CACHE_BACKEND"),
        "LOCATION": get_env_variable("CACHE_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": get_env_variable("CACHE_KEY_PREFIX")
    }
}

# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15

# CELERY STUFF
BROKER_URL = get_env_variable("BROKER_URL")
CELERY_RESULT_BACKEND = get_env_variable("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

# cacheops
CACHEOPS_REDIS = {
    'host': get_env_variable("CACHEOPS_HOST"),
    'port': get_env_variable("CACHEOPS_PORT"),
    'db': get_env_variable("CACHEOPS_DB"),
    'socket_timeout': 3,
}

CACHEOPS_DEGRADE_ON_FAILURE = True

# STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, "school/config/gcp_bucket_config.json")
)

# STORAGE BUCKET
DEFAULT_FILE_STORAGE = get_env_variable("DEFAULT_FILE_STORAGE")
GS_BUCKET_NAME = get_env_variable("GS_BUCKET_NAME")
GS_LOCATION = get_env_variable("GS_LOCATION")
GS_DEFAULT_ACL = get_env_variable("GS_DEFAULT_ACL")
GS_FILE_OVERWRITE = get_env_variable("GS_FILE_OVERWRITE")
print(GS_FILE_OVERWRITE)

# Mail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = get_env_variable("EMAIL_USE_TLS")
EMAIL_PORT = get_env_variable("EMAIL_PORT")
