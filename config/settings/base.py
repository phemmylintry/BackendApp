"""
Django settings for test project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import environ
import datetime
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('keel')
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    env.read_env(str(ROOT_DIR.path('.env')))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# Custom User model
AUTH_USER_MODEL = 'authentication.User'

# AUTHENTICATION_BACKENDS = ('keel.authentication.backends.AuthBackend',)

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG', False)

TIME_ZONE = 'Asia/Kolkata'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FILE_UPLOAD_PERMISSIONS = 0o664
# FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ENGINE'] ='django.db.backends.postgresql_psycopg2'

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
)

THIRD_PARTY_APPS = (

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'import_export',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'rest_auth',
    'rest_auth.registration',
    'ckeditor',
)


LOCAL_APPS = (
    'keel.crm',
    'keel.authentication',
    'keel.leads',
    'keel.eligibility_calculator',
    'keel.document',
    'keel.Core',
    'keel.plans',
    'keel.tasks',
    'keel.cases',
    'keel.chats',
    'keel.quotations',
    'keel.notifications',
    'keel.calendly',
    'keel.call_schedule',
    'keel.payment',
    'keel.stripe',
    'keel.questionnaire',
    'keel.records',
    'keel.web',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


CORS_ORIGIN_ALLOW_ALL = True

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

SOCIALACCOUNT_ADAPTER = "keel.api.v1.auth.adapter.MySocialAccountAdapter"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook':
        {'METHOD': 'oauth2',
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERSION': 'v2.4'
    },
    'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'keel.middleware.RequestErrorLogging.RequestErrorLoggingMiddleware',
    'keel.middleware.request_utils.RequestMiddleware',
]


ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# APP_DIRS = True

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = str(ROOT_DIR('static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
     str(APPS_DIR.path('static')),
 )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = str(ROOT_DIR('media'))

SITE_ID = 1

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('static')),
        ],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                ]),

            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'PAGE_SIZE': 10,
    'COERCE_DECIMAL_TO_STRING': True,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'keel.authentication.backends.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )

}
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'app-name', 'limit', 'offset', 'redirect']

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'bearer',
    'JWT_EXPIRATION_DELTA' : datetime.timedelta(seconds=300),
}

USER_SECRET_KEY = "secret"

BASE_URL = env('BASE_URL')
ADMIN_BASE_URL = env('ADMIN_BASE_URL')
APPEND_SLASH=True
API_BASE_URL = env('API_BASE_URL')
# CONN_MAX_AGE=600

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AWS_STATIC_LOCATION=''
AWS_PUBLIC_MEDIA_LOCATION=''
AWS_PRIVATE_MEDIA_LOCATION=''
PRIVATE_FILE_STORAGE='django.core.files.storage.FileSystemStorage'

DEFAULT_USER_PASS = env('DEFAULT_USER_PASS')

# Calendly settings
CALENDLY_PERSONAL_TOKEN = env('CALENDLY_PERSONAL_TOKEN')
CALENDLY_BASE_URL = env('CALENDLY_BASE_URL')
CALENDLY_SIGNING_KEY = env('CALENDLY_SIGNING_KEY')
CALENDLY_ORGANIZATION_URL = env('CALENDLY_ORGANIZATION_URL')

STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SIGNING_SECRET = env('STRIPE_WEBHOOK_SIGNING_SECRET')

# REDIS SETTINGS
REDIS_HOST=env("REDIS_HOST")
REDIS_PORTNAME=6379
REDIS_DBNAME=0

# RAZOR PAY SETTINGS
RAZORPAY_KEY_ID = env('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = env('RAZORPAY_KEY_SECRET')