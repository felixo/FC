"""
Django settings for FC project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&2@4=m)edh8^-kj^bgb)*=y!5k%uqfhmko#khxo0ih4rbx$v+u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
	'www.fabercastellgottalent.ru',
	'www.fabercastellgottalent.com',
	'fabercastellgottalent.ru',
	'fabercastellgottalent.com',
	'xn--80aaaacyba0arnad3a8asrfaew6j6b.xn--p1ai/',
	'xn--80aaaacyba0arnad3a8asrfaew6j6b.xn--p1ai',
	'localhost',
	'138.201.116.120',
	'127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'fcgt.apps.FcgtConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FC.urls'

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

WSGI_APPLICATION = 'FC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'FC',
    #     'USER': 'root',
    #     'PASSWORD': '1236969',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data3.db'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social_core.apps.django_app.context_processors.backends',
   'social_core.apps.django_app.context_processors.login_redirect',

)

AUTHENTICATION_BACKENDS = (
   'social_core.backends.facebook.FacebookOAuth2',
   'social_core.backends.google.GoogleOAuth2',
   'social_core.backends.twitter.TwitterOAuth',
   'social_core.backends.vk.VKOAuth2',
   'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
   'django.contrib.auth.backends.ModelBackend',

)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '277557235920116'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c009f53d9fa3e3483d84498f027d2c74'

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'BeGboVvfquYYdH8zgGqUKA4rM'
SOCIAL_AUTH_TWITTER_SECRET = 'iDdIuFkhDrbAeb8h4f6UavBU0a4TS46cEpfnoZNzrvxLO907En'

SOCIAL_AUTH_VK_OAUTH2_KEY = '5481988'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'R7OvLoHoscfHBOZZ4hsy'

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = ''
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = ''
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '68597720710-atcadbtuc2mbrdojskb18j3tbr46ch6v.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'NfMwX3-8D8EG68BxLE8Rh_Nb'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SOCIAL_AUTH_RAISE_EXCEPTIONS = False
