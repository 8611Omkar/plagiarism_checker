DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Delta',
        'USER': 'root',
        'PASSWORD': 'Omkar@8611',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # Other middleware...
]

INSTALLED_APPS = [
    # Default installed apps...
]

INSTALLED_APPS += ["django_extensions"]

