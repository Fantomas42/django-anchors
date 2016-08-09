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
]

SECRET_KEY = 'secret-key'

STATIC_URL = '/'
