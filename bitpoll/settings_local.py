import os
BASE_DIR="/Bitpoll"
ROOT_DIR=BASE_DIR
ALLOWED_HOSTS= ["*"]

# You must insert your own random value here
# SECURITY WARNING: keep the secret key used in production secret!
# see <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#secret-key>
SECRET_KEY = '45201fd8-b978-11e7-af78-50e549b7152c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Add additionall installed apps here
INSTALLED_APPS_LOCAL = []

LANGUAGE_CODE = 'de-DE'
TIME_ZONE = 'Europe/Berlin'

## https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'dbbitpoll',
        'PORT': 3306,
        'NAME': 'bitpoll',
        'USER': 'bitpoll',
        'PASSWORD': '3f279580-b97c-11e7-b638-50e549b7152c'
    }
}

## Customize your instance
SITE_NAME = 'Bitpoll - WIAI'
BASE_URL = 'https://bitpoll.wiai.de'

## Url to the Base Homepage and Text on the Link, leave empty to not use this option
HOME_URL = "https://bipoll.wiai.de"
HOME_URL_NAME = "Dashboard"

## Test mail functionality by printing mails to console:
## EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

## if the imprint URL is not empty use it as an link to the imprint, else use IMPRINT_TEXT
#IMPRINT_URL = ""
#IMPRINT_TEXT = """
#<h1>ImpressuXm</h1>
#<p>Text goes here</p>
#"""

#LOCALE_PATHS = (os.path.join(ROOT_DIR, 'locale'), )
#LANGUAGES = (
#    ('de', 'Deutsch'),
#    ('en', 'English'),
#    #('fr', 'Français'),
#)

#REGISTER_ENABLED = True
#GROUP_MANAGEMENT = REGISTER_ENABLED

## Use ldap login
import ldap
from django_auth_ldap.config import LDAPSearch

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

AUTH_LDAP_SERVER_URI = "ldap://ldap.wiai.de/"
AUTH_LDAP_BIND_DN = "ldap_bind_dn"
AUTH_LDAP_BIND_PASSWORD = "ldap_bind_pw"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=people,ou=fswiai,dc=ldap,dc=wiai,dc=de",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_ALWAYS_UPDATE_USER = True

from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=people,ou=fswiai,dc=ldap,dc=wiai,dc=de",
    ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"
    )
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
#AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_MIRROR_GROUPS = True

AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email": "mail"}

#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    "is_staff": ["cn=Editoren,ou=groups,dc=mafiasi,dc=de",
#                 "cn=Server-AG,ou=groups,dc=mafiasi,dc=de"],
#    "is_superuser": "cn=Server-AG,ou=groups,dc=mafiasi,dc=de"
#}
import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)