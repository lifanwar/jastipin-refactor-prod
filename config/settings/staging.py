from .base import *
import os

DEBUG = False  # Bisa True untuk staging testing

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database - PostgreSQL untuk staging
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'sslmode': 'require'
    },
    }
}

# CSRF_TRUSTED_ORIGINS = [
#     f'https://{DOMAIN}',
#     f'http://{DOMAIN}',
# ]
