""" Settings of YAUS Project"""
import environ
# from pathlib import Path
import os
import django_heroku
from datetime import timedelta

#Parth of root dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env") #path of .env file
environ.Env.read_env(env_file) # reading .env file



# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = [ '*' ]

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


DATABASES = {'default': env.db('DATABASE_URL')} #Read database in env


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())