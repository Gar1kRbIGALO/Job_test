import os
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'igor',
        'PASSWORD': 'rjpytdf72',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    'books',
]

settings.configure(
    DATABASES=DATABASES,
    INSTALLED_APPS=INSTALLED_APPS,
)
django.setup()
