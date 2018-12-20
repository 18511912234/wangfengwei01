"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

#项目路径：保持默认即可不需要修改，通过0o模块读取当前项目在系统的具体目录
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

#秘钥配置，这是一个随机值，主要用于数据的加密处理，提高系统的安全性，避免遭到攻击者的恶意破坏
#秘钥主要用于：用户密码，CRSF机制，会话session等
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$8^0=ehgb%ve#6pcz7l6$=w$yl829o88#e+n5ld16tv33x6^dp'

# SECURITY WARNING: don't run with debug turned on in production!

#调试模式配置:开发过程设置为True，上线时候设置为False，否则会泄漏系统相关信息
DEBUG = True

#域名访问权限配置：设置可以访问的域名，当DEBUG = True时且ALLOWED_HOSTS = []时，只允许localhost和127.0.0.1访问
#当DEBUG = False时ALLOWED_HOSTS为必填项
#如果允许所有域名访问，设置为：ALLOWED_HOSTS=['*']
ALLOWED_HOSTS = []


#应用列表配置：将应用的名字添加到该列表中
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #新的应用
    'index',
    'user'
]

#中间件配置, 每个中间件的设置顺序是固定的
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',#内置安全机制，保护用户与网站的通信安全
    'django.contrib.sessions.middleware.SessionMiddleware',#回话session功能
    #使Django的内置功能支持中文显示，添加如下配置
    'django.middleware.locale.LocaleMiddleware',#支持中文语言

    'django.middleware.common.CommonMiddleware',#处理请求信息
    #'django.middleware.csrf.CsrfViewMiddleware',#开启CSRF防护
    'django.contrib.auth.middleware.AuthenticationMiddleware',#开启内置用户认证系统
    'django.contrib.messages.middleware.MessageMiddleware',#开启内置信息提示功能
    'django.middleware.clickjacking.XFrameOptionsMiddleware',#防止恶意程序点击劫持2
]

ROOT_URLCONF = 'MyDjango.urls'

#模板配置信息
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #设置模板所在的路径,这里存的是列表，可以配置多个模板路径
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR,'index/templates/admin/index')],
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

WSGI_APPLICATION = 'MyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#数据库配置
DATABASES = {
    #第一个数据库
    'default': {
        #mysql数据库，python3不支持mysqldb，支持mysqlclient
        'OPTIONS':{'isolation_level':None},
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'wfw_test',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        #'HOST':'10.7.0.113',
        'PORT':'3306',
    },
    #第二个数据库,多个库不同的表怎么使用
    # 'MyDjango':{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME':'MyDjango_db',
    #     'USER':'root',
    #     'PASSWORD':'123456',
    #     'HOST':'127.0.0.1',
    #     'PORT':'3306',
    # },
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

'''
静态文件配置方法1：
1.在应用下新建static目录
2.在static目录下再新建图片，js，css等目录
3.把该应用相关的静态资源放到到对应的目录下即可
4.这样配置浏览器可以直接通过目录直接访问，而且不需要添加其他配置
'''
STATIC_URL = '/static/'

'''
静态资源配置方法2：
1.在项目的根目录下新建静态资源文件夹：public_static
2.在对应的应用目录下新建static目录
3.在static目录下新建图片，css，js等目录
4.把对应的静态资源放入到对应的文件夹中
5.进行配置：STATICFILES_DIRS=[os.path.join(BASE_DIR,'public_static'),os.path.join(BASE_DIR,'index/static')]
'''
#路径拼接
STATICFILES_DIRS=[os.path.join(BASE_DIR,'public_static'),os.path.join(BASE_DIR,'index/static')]



#配置邮箱
EMALL_USE_SSL=True
#邮件服务器(这个是163邮箱的)
EMAIL_HOST='stmp.163.com'
#邮件服务器端口
EMAIL_PORT=465
#发送邮件的账号
EMAIL_HOST_USER='w18511912234@163.com'
#SMTP授权码 不是邮箱密码
EMAIL_HOST_PASSWORD='wangfengwei1'
#设置默认发送邮件的邮箱
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER