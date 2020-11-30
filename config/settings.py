import os


###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = os.path.basename(BASE_DIR)

#####################
# Security settings #
#####################

SECRET_KEY = 'q7cd30q)ec*+dk#flh#o0w16mdad3cd$=1o!c9wfktelgv+u-!'

DEBUG = True

ALLOWED_HOSTS = ['*']


#################
# Core settings #
#################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',

    # apps
    'accounts.apps.AccountsConfig',
    'shiftapp.apps.ShiftappConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
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

WSGI_APPLICATION = 'config.wsgi.application'


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###########
# Logging #
###########

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'develop': {
#             'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
#                       '%(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'develop',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         # 'django.db.backends': {
#         #     'handlers': ['console'],
#         #     'level': 'DEBUG',
#         #     'propagate': False,
#         # },
#     },
# }


################
# Static files #
################

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


##################
# Authentication #
##################

AUTH_USER_MODEL = 'accounts.User'

# 認証方式を「メールアドレスとパスワード」に変更
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ユーザー名は使用しない
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# ユーザー登録確認メールは送信しない
ACCOUNT_EMAIL_VERIFICATION = 'none'
# メールアドレスを必須項目にする
ACCOUNT_EMAIL_REQUIRED = True

SITE_ID = 1

LOGIN_REDIRECT_URL = 'index'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'


##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#################
# debug toolbar #
#################

if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
