# Django settings for sqwag project.
import os.path
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nikhiltyagi.eng@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqwag-dj',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

CONTENT_BASE = os.path.join(PROJECT_ROOT, 'assets')
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(CONTENT_BASE, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
TWITTER_CONSUMER_KEY = 'pZ7xPQJlkzaCxW73p276zw'
TWITTER_CONSUMER_SECRET = 'fIkFmEyL7aI8k0YVAYK4xL4ZXoYQevHAvmipMEdCU9s'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_AUTHORIZE_URL ='https://api.twitter.com/oauth/authorize'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
CALLBACK_URL = 'http://127.0.0.1:8000/'

INSTA_CLIENT_ID = '6e7b6c7542284c31b55679862df1e11e'
INSTA_CLIENT_SECRET = '03ba3c5c66f24d5b8357852d66c02eb7'
INSTA_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize/?'
INSTA_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
INSTA_WEBSITE_URL = 'http://betadev1.sqwag.com'
INSTA_CALLBACK_URL = 'http://betadev1.sqwag.com/sqwag/accessinsta/'

INSTA_SUBSCRIPTION_URL = 'https://api.instagram.com/v1/subscriptions/'
INSTA_SUBS_CALLBACK_URL= 'http://betadev1.sqwag.com/sqwag/instacb/'

FACEBOOK_APP_ID = '358855170845635'
FACEBOOK_APP_SECRET = 'b1f164a2d85cc34f49967e9c14720798'
FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?'
FACEBOOK_AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth/?'
FACEBOOK_CALLBACK_URL = 'http://127.0.0.1:8000/sqwag/accessfacebook/'
FACEBOOK_CALLBACK_URL_NEW_USER = 'http://127.0.0.1:8000/sqwag/accessfacebooknewuser/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=*ht8yidb^_^6g#kkzbed0roqr9_7e&#e_edex#co1n3txuf8_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "./templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sqwag_api',
    'sorl.thumbnail',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SQWAG_TWITTER_USER = 'sqwaglc'
SQWAG_USER_ID = 44  #kind of misleading name. this is user's id in auth_user table
AUTH_PROFILE_MODULE = "sqwag_api.UserProfile"
