# -*- coding: utf-8 -*-
from datetime import timedelta

DEBUG = TEMPLATE_DEBUG = True

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db',
    }
}

USE_TZ = False

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sites',
    'cms',
    'menus',
    'app',
    'sekizai',
    'mptt',
]

ROOT_URLCONF = 'urls'

CMS_TEMPLATES = [
    ('tpl.html', 'tpl.html'),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
     "django.core.context_processors.debug",
     "django.core.context_processors.request",
     "django.core.context_processors.i18n",
     "django.core.context_processors.media",
     "django.core.context_processors.static",
     "django.core.context_processors.tz",
     "django.contrib.messages.context_processors.messages",
     "sekizai.context_processors.sekizai",
]

LANGUAGES = [('en', 'en')]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
]
