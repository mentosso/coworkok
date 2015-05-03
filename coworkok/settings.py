import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'vvj&+a94!^+aa%2ghr#!2o*)kzn)bnl4m*!6zrab3(a2$l)!^0'
DEBUG = True

ALLOWED_HOSTS = []

# Miscellaneous
SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('cowork:dashboard')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

GENERIC_APPS = (
    'authtools',
    'pipeline',
)

LOCAL_APPS = (
    'accounts',
    'cowork',
)

INSTALLED_APPS += LOCAL_APPS + GENERIC_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'coworkok.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'coworkok', 'templates'),
        ],
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

WSGI_APPLICATION = 'coworkok.wsgi.application'


# Database

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'coworkok',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'marcin',
            'PASSWORD': 'marcin',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


# Django Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE = True
PIPELINE_AUTO = True
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'dashboard': {
        'source_filenames': (
            'cowork/less/dashboard.less',
        ),
        'output_filename': 'cowork/less/dashboard.css'
    },
    'accounts': {
        'source_filenames': (
            'accounts/less/accounts.less',
        ),
        'output_filename': 'accounts/less/accounts.css'
    }
}
