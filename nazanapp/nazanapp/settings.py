from pathlib import Path
import os  # os modülü static path için gerekli

# Proje ana dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# Güvenlik
SECRET_KEY = 'django-insecure-f9m=rbq(a-o!a+lzky+0%#cy9i7c5^l=h+$je!4rrl)0a7ww-^'
DEBUG = True
ALLOWED_HOSTS = [DEBUG = False

ALLOWED_HOSTS = ['*']]

# Uygulamalar
INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL yönlendirme
ROOT_URLCONF = 'nazanapp.urls'

# Şablonlar
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # manuel template klasörü
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

# WSGI
WSGI_APPLICATION = 'nazanapp.wsgi.application'

# Veritabanı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parola doğrulayıcılar
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

# Uluslararasılaştırma
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Statik dosyalar (CSS, JS, img)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Eğer production'a geçersen şu satırı da açarsın:
# STATIC_ROOT = BASE_DIR / "staticfiles"

# Varsayılan model ID alanı
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
