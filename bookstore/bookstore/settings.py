"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

# 　将项目的目录设置为根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将所有的模块配置到apps
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# django产生的密钥，用来csrf_token，或者对密码进行加密时，作为种子，加盐加密
SECRET_KEY = '!wmny(x@pmwo&h36*w47=)-h+f+38w+ecdq*3im!a9w_@ryi)z'

# SECURITY WARNING: don't run with debug turned on in production!
# 浏览器直接看到报错信息
DEBUG = True

# 允许访问的host
ALLOWED_HOSTS = ['*']

# Application definition
# 安装的app
INSTALLED_APPS = (
    'django.contrib.admin',  # django自带的后台管理系统
    'django.contrib.auth',  # 鉴权
    'django.contrib.contenttypes',  # 包装response，比如text/html，image/gif
    'django.contrib.sessions',  # 处理session和cookie
    'django.contrib.messages',  # 日志系统
    'django.contrib.staticfiles',  # 静态文件处理器
    'users',  # 用户模块
    'books',  # 商品模块
    'tinymce',  # 富文本编辑器
    'order',  # 订单信息模块
    'comments',  # 评论模块
    'haystack',  # 全文检索框架
    'users.templatetags.filters',  # 过滤器功能
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',  # 处理session的中间件
    'django.middleware.common.CommonMiddleware',  # 基本功能
    'django.middleware.csrf.CsrfViewMiddleware',  # 跨域
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 鉴权
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'utils.middleware.BookMiddleware',
    'utils.middleware.AnotherMiddleware',
    'utils.middleware.UrlPathRecordMiddleware',
    'utils.middleware.BlockedIpMiddleware',
)

ROOT_URLCONF = 'bookstore.urls'  # 主应用的url路由

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 这里别忘记配置！
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
# uwsgi接收到请求以后，解析成django可以处理的格式，部署的时候使用
WSGI_APPLICATION = 'bookstore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 配置为mysql
        'NAME': 'bookstore',  # 数据库的名字
        'USER': 'root',  # 用户名
        'PASSWORD': 'mysql',  # 密码
        'HOST': '127.0.0.1',  # host
        'PORT': 3306,  # 端口
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'  # 静态文件的路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]  # 调试时使用的静态文件目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
# 上传文件指定的路径，在生产环境中会上传到CDN，七牛云，又拍云，阿里云，也有可能将静态文件放在nginx的服务器上．
MEDIA_ROOT = os.path.join(BASE_DIR, "static")

# 邮件的相关配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'zuoyuantc@126.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'xxxxxxxx'
# 收件人看到的发件人
EMAIL_FROM = 'bookstore<zuoyuantc@126.com>'

# 富文本编辑器相关配置
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

# pip install django-redis
# 缓存相关配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",  # 第二个数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": ""
        }
    }
}

# session使用redis进行缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 全文检索配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6  # 指定搜索结果每页的条数

ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/log/debug.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
