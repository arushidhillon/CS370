"""
Django settings for research_match project.
Generated by 'django-admin startproject' using Django 4.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import mimetypes
mimetypes.add_type("text/css", ".css", True)
from django.contrib.messages import constants as messages
import os
import dj_database_url
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from whitenoise.storage import CompressedManifestStaticFilesStorage
BASE_DIR = Path(__file__).resolve().parent.parent


# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOCAL_DEBUG = False

if LOCAL_DEBUG:
    # Debug Keys
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-9h#qg6t@pxdf3&nypr1k%!a!8myas-g)26*&!bo#wy#3#-85)h'
    ENCRYPT_KEY = b'WIuRycBTSZ9VVevuPE4kXdnwVUlVrC7p1qZTDgFx-Sc='

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
else:
    # Keys
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ENCRYPT_KEY = os.environ.get('ENCRYPT_KEY')

    DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)
    


#ENCRYPT_KEY = b'WIuRycBTSZ9VVevuPE4kXdnwVUlVrC7p1qZTDgFx-Sc='


#Configure
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ionos.com'  # IONOS SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'deadline.tech@research-match.com'
EMAIL_HOST_PASSWORD = os.getenv('IONOS_KEY')
EMAIL_DEBUG = True  


ALLOWED_HOSTS = ['research-match-c2c44e3d1621.herokuapp.com', "127.0.0.1"]
# Application definition
INSTALLED_APPS = [
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profilepage',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'crispy_forms',
    'search',
    'inbox',
    'django_htmx',
]

class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]



ROOT_URLCONF = 'research_match.urls'
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = "/"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS" : {
            "min_length": 8,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates", "inbox/templates"],
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
#AUTH_USER_MODEL = 'profilepage.User'