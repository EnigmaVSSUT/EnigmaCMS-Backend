import os
from pathlib import Path
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
with open(os.path.join(BASE_DIR, 'credentials.json')) as credentials_file:
    credentials = json.load(credentials_file)


def get_secret(setting, secrets=credentials):
    """Get secret settings or fail with Improperly configured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

def get_db(type, setting, secrets=credentials):
    """Get secret settings or fail with Improperly configured"""
    try:
        return secrets[type][setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'courses',
    'members',
    'projects',
    'events',
    'baton',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    # 'django_graphene',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cms_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cms_backend.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_db('QA_DATABASE', 'NAME'),
        'HOST': get_db('QA_DATABASE', 'HOST'),
        'USER': get_db('QA_DATABASE', 'USER'),
        'PASSWORD': get_db('QA_DATABASE', 'PASSWORD')
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static',),)
STATIC_URL = '/static/'

# Default primary key field type
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_EMAIL_VERIFICATION = 'none'
SITE_ID = 1
LOGIN_URL = 'account_login'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# ACCOUNT_UNIQUE_EMAIL = True


# django Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.in'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

GRAPHENE = {
    'SCHEMA': 'cms_backend.Schema.Schema'
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'members.serializers.LoginUserSerializer',
}
AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_SIGNATURE_VERSION = get_secret('AWS_S3_SIGNATURE_VERSION')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DATA_UPLOAD_MAX_MEMORY_SIZE = 429916160

CORS_ORIGIN_ALLOW_ALL = True
