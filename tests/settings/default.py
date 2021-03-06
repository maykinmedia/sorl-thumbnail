from os.path import join as pjoin, abspath, dirname, pardir

PROJ_ROOT = abspath(pjoin(dirname(__file__), pardir))
DATA_ROOT = pjoin(PROJ_ROOT, 'data')
THUMBNAIL_PREFIX = 'test/cache/'
THUMBNAIL_DEBUG = True
THUMBNAIL_LOG_HANDLER = {
    'class': 'sorl.thumbnail.log.ThumbnailLogHandler',
    'level': 'ERROR',
}
THUMBNAIL_KVSTORE = 'thumbnail_tests.kvstore.TestKVStore'
THUMBNAIL_STORAGE = 'thumbnail_tests.storage.TestStorage'
DEFAULT_FILE_STORAGE = 'thumbnail_tests.storage.TestStorage'
ADMINS = (
    ('Sorl', 'thumbnail@sorl.net'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'thumbnail_tests',
    }
}
MEDIA_ROOT = pjoin(PROJ_ROOT, 'media')
MEDIA_URL = '/media/'
ROOT_URLCONF = 'thumbnail_tests.urls'
INSTALLED_APPS = (
    'thumbnail',
    'thumbnail_tests',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
)

SECRET_KEY = 'v2824l&2-n+4zznbsk9c-ap5i)b3e8b+%*a=dxqlahm^%)68jn'
