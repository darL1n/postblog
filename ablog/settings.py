

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oln6e5@hw1x-jnwek_li0gRSxEx706=8dk2dw83i&9xpz*=eb-ab2+o0+0qi53l6k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['185.117.155.100' , 'micolux.ru' , 'www.micolux.ru' , 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'theblog',
    'members',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'hitcount',
    'components',
    'crispy_forms',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ablog.urls'

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
                'theblog.context_processors.menu_categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'ablog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bloglux',
        'USER': 'mico',
        'PASSWORD': 'mico12lux23',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_DIR = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
CKEDITOR_CONFIGS = {
'default': {
    'width':  'auto',
}
}
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'frontpage'
LOGOUT_REDIRECT_URL = 'frontpage'

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'gamer97abk@mail.ru'
EMAIL_HOST_PASSWORD = 'myspace.com.1997.23.12'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

