# add this to the import section of the file
import os

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Handling Key Import Errors
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party apps
    'cacheops',
    'rest_framework',
    'knox',
    'corsheaders',
    # my apps
    'frontend',
    'library',
    'staff',
    'academics',
    'students',
    'accounts',
    'examinations',
    'assignments',
    'mail',
    'sms'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'school.urls'

WSGI_APPLICATION = 'school.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/frontend/static"),
]
STATIC_ROOT = "static/"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media
MEDIA_URL = '/storage/'
MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

# authentication

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
}

# cacheops
CACHEOPS = {
    'auth.user': {'ops': 'get', 'timeout': 60 * 15},
    'assignments.*': {'ops': (), 'timeout': 60 * 60},
    'students.*': {'ops': (), 'timeout': 60 * 60},
    'library.*': {'ops': (), 'timeout': 60 * 60},
}
