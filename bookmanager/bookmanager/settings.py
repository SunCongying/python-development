"""
Django settings for bookmanager project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'av)mx+bxie^5i_e5_d0^0zb%jhc3eef%p40kt1+u0-10+1gp$s'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
# 在开发时开启debug模式可以看到更多的信息，
# 当程序上线后就关闭debug，因为debug会消耗一些资源
# 关闭debug需要设置ALLOWED_HOSTS
DEBUG = True

# 允许以什么形式访问我们的项目，*的意思是可以使用ip，也可以使用127，一般不用127
# 默认本机 127.0.0.1
ALLOWED_HOSTS = ['*']


# Application definition
# 注册/安装子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'book', # 手动输入  方案1
    'book.apps.BookConfig'  # 方案2
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

ROOT_URLCONF = 'bookmanager.urls'

# 模板配置相关的
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 给出模板文件所在的文件夹位置
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

WSGI_APPLICATION = 'bookmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# sqlite3也是一个关系型数据库，主要用于移动端，了解即可
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 设置网页显示的语言
LANGUAGE_CODE = 'zh-Hans' #'en-us'
# 设置时区
TIME_ZONE = 'Asia/Shanghai' #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 访问静态资源的路由
STATIC_URL = '/static/'  # 可以自定义路由

# 静态资源的位置
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static'),
]