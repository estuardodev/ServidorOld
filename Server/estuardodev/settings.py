"""
Django settings for estuardodev project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*5)r*hu5^1=2d@8&xex-#1=e5$sri+k+p2ap83=01!zyj!d_da'

# SECURITY WARNING: don't run with debug turned on in production!

debug_txt = os.path.join(BASE_DIR, 'debug.txt') # Se necesita debug.txt en la carpeta /Servidor/Server/ 
with open(debug_txt, 'r') as D:
    read_debug = D.read()
lista = list(read_debug)
lista.pop()

for i in lista:
    if i == '0':
        entorno = True
    else:
        entorno = False
if entorno == True:
    DEBUG = False
else:
    DEBUG = True


# ALLOWED_HOSTS = ['estuardodev.com', 'www.estuardodev.com'] # Local
ALLOWED_HOSTS = ['estuardodev.com', 'www.estuardodev.com', 'blog.estuardodev.com'] # Production
CSRF_TRUSTED_ORIGINS = ['https://estuardodev.com']

# Application definition

INSTALLED_APPS = [
    # TERCEROS
    'django_hosts',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # PROPIAS
    'portafolio.apps.PortafolioConfig',
    'legal.apps_legal.LegalConfig',
    'blog.apps_blog.BlogConfig',
    
]

MIDDLEWARE = [
    # Django hosts
    'django_hosts.middleware.HostsRequestMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Django hosts
    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'estuardodev.urls'

# Django hosts
ROOT_HOSTCONF = 'estuardodev.hosts'
DEFAULT_HOST = 'www'

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

WSGI_APPLICATION = 'estuardodev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_app',
        'USER': 'root',
        'PASSWORD': 'MDB_Root_1',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

SITE_ID = 1 

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-gt'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
