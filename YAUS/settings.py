""" Settings of YAUS Project"""
from pathlib import Path
import os
import django_heroku
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ndds9!(0@qr!g^8$4ifcbnyiaumlx^(1q!62ko#s6d12ts2eqj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False    

ALLOWED_HOSTS = [ '*'
]

# Application definition

INSTALLED_APPS = [
    #Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Djangorest-Framework
    'rest_framework',
    'rest_framework.authtoken',
    #apps created
    'api',
    #knox auth
    'knox',
    #authKnox
    'authKnox',
    #cors handling
    'corsheaders',
    #Api Analytics
    'api_analytics',
]

REST_FRAMEWORK = {
    #Authentication system
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'knox.auth.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
    ),

    #Rate Limiting
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
        'anon_register_url': '1/day',
        'anon_login': '100/minute',

        'user': '100/minute',
        'developer_register_url': '100/minute',
        'common_register_url':'10/minute',
    },
    
    #Pagiination 
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': timedelta(hours=1),
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
    'TOKEN_LIMIT_PER_USER': 100,
    'AUTO_REFRESH': True
}


MIDDLEWARE = [
    #cors manage
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
        
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Cors configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'YAUS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'YAUS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd1q7fco1bj2t7k',
        'USER': 'bzkcnoarxfnwoy',
        'PASSWORD': '844e218b3a5c3baaf1802567961a80d6e4c8e31b5870bc03ef8d58014fb362a1',
        'HOST':'ec2-107-20-104-234.compute-1.amazonaws.com',
        'PORT':'5432',
        'CONN_MAX_AGE': 10,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())
