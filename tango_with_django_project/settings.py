"""
Django settings for tango_with_django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
# added -------------------------------------------------

# using TEMPLATE_PATH as we should always use absolute paths not 
# relative paths
TEMPLATE_DIRS = [TEMPLATE_PATH,]
# -------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v8k6@99q+*ukcq_ryni958fs&6sg3jn4o)u&88y!@n98!_-npn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth', # provides Django with access to the authentication system
    'django.contrib.contenttypes', # used by the authentication application to track models in your database 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
    'Bao',
    'registration',
)

MIDDLEWARE_CLASSES = (
    # sessionMiddleware enables the creatio of unique session id cookies
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'

# if your application requires more contol over how passwords are hashed

#PASSWORD_HASHERS = (
#    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # an absolute path to the media directory


REGISTRATION_OPEN = True # if true the users can register
ACCOUNT_ACTIVATION_DAYS = 7 # one week after activation window.
REGISTRATION_AUTO_LOGIN = True # if true, the users will be automatically logged in.
LOGIN_REDIRECT_URL = '/Bao/' # the page you want users to arrive at if they sucessfully login.

# redirects users that try to access restricted areas
LOGIN_URL = '/accounts/login/'



