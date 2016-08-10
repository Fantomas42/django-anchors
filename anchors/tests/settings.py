"""Settings for testing anchors"""

DATABASES = {
    'default': {'NAME': 'emoticons.db',
                'ENGINE': 'django.db.backends.sqlite3'}
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }
]

INSTALLED_APPS = [
    'anchors',
    'django.contrib.sites',
]

SITE_ID = 1

SECRET_KEY = 'secret-key'

STATIC_URL = '/'
