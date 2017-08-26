#coding:utf-8
import os


# Repository directory.
ROOT = os.path.dirname(os.path.dirname(__file__))

# use config,DEBUG and DATABASES in it


try:
    from stucampus.config.production import *
except ImportError:
    from stucampus.config.development import *

# path bases things off of ROOT
def path(*a):
    return os.path.abspath(os.path.join(ROOT, *a))

# DjangoUeditor setting
UEDITOR_SETTINGS = {
    "images_upload":{
        'allow_type': 'jpg, png, gif, JPG, PNG, GIF',
        'path': 'img_upload_file/',
        'max_size': '3000kb',
        },
    }


ALLOWED_HOSTS = ["*"]
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = '/account/signin'

MEDIA_ROOT = path(ROOT, 'webroot', 'media')


MEDIA_URL = '/media/'

STATIC_ROOT = path(ROOT, 'webroot', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path('stucampus', 'static'),
)



QINIU_ACCESS_KEY = '4JBSsVDFK80Vu6c3f36AtEYl-5wadK-ZoWb-os5w'
QINIU_SECRET_KEY = 'F8bNfqtPKrlgswQfCqaKGsftm8ZCE12r5ySTsEXJ'
QINIU_BUCKET_NAME = 'jimczj'
QINIU_BUCKET_DOMAIN = '7xsx9g.com1.z0.glb.clouddn.com'
QINIU_SECURE_URL = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path('stucampus', 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
            'debug': DEBUG,
        },
    },
]

ROOT_URLCONF = 'stucampus.urls'

WSGI_APPLICATION = 'stucampus.wsgi.application'

#用于login_szu的配置

LOGIN_SZU_SECURE_URL=False#或True
LOGIN_SZU_BUCKET_DOMAIN="stu.szu.edu.cn"




MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'stucampus.middleware.PutHTTPMethodDataMiddleware',
    #'stucampus.middleware.qiniu.QiniuMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',
    'DjangoUeditor',
    'stucampus.master',
    'stucampus.account',
    'stucampus.infor',
    'stucampus.organization',
    'stucampus.lecture',
    'stucampus.activity',
    'stucampus.articles',
    'stucampus.magazine',
    'stucampus.spider',
    'stucampus.szuspeech',
    'stucampus.minivideo',
    'stucampus.carousels',
    'stucampus.member_infor',
    'stucampus.summer_plans',

    'stucampus.dreamer',
    'stucampus.FreeTimeCount',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'stucampus.gobye',
    'stucampus.board',
    #'stucampus.christmas',
    'stucampus.wechat',
    'stucampus.comment',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '''[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s]
                         %(message)s''',
            'datefmt': "%d/%b/%Y %H:%M:%S"
         }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'stucampus_error.log',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'stucampus': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
SESSION_EXPIRE_AT_BROWSER_CLOSE=False
SESSION_COOKIE_AGE=16538400 #半年 
# django 发送邮件配置，用于summer_plans
EMAIL_HOST=u'smtp.aliyun.com'
EMAIL_HOST_USER=u'szudatalab@aliyun.com'
EMAIL_HOST_PASSWORD=u'szudatalab01'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = u'[深圳大学学子天地]'
DEFAULT_CHARSET="utf-8"

DUOSHUO_SHORT_NAME="szustu" #多说二级域名
