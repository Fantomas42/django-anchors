"""Settings for the anchors demo"""
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

STATIC_URL = '/static/'

SECRET_KEY = 'secret-key'

ROOT_URLCONF = 'anchors.demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT],
        'APP_DIRS': True,
    }
]

INSTALLED_APPS = [
    'anchors',
    'django.contrib.staticfiles'
]
