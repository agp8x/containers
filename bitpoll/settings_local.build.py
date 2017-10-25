import os
BASE_DIR="/Bitpoll"
ROOT_DIR=BASE_DIR
ALLOWED_HOSTS= ["*"]

# You must insert your own random value here
# SECURITY WARNING: keep the secret key used in production secret!
# see <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#secret-key>
SECRET_KEY = '...'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Add additionall installed apps here
INSTALLED_APPS_LOCAL = []

#LANGUAGE_CODE = 'de-DE'
#TIME_ZONE = 'Europe/Berlin'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

## Customize your instance
#SITE_NAME = 'Bitpoll'
#BASE_URL = 'https://example.com'

## Url to the Base Homepage and Text on the Link, leave empty to not use this option
#HOME_URL = "https://example.com"
#HOME_URL_NAME = "Dashboard"
