from storages.backends.s3boto import S3BotoStorage
from django.conf import settings

S3_MEDIA_ROOT = getattr(settings, 'S3_MEDIA_PATH', 'media')
S3_STATIC_ROOT = getattr(settings, 'S3_STATIC_PATH', 'static')
S3_MEDIA_FILE_OVERWRITE = getattr(settings, 'S3_MEDIA_FILE_OVERWRITE', False)
S3_STATIC_FILE_OVERWRITE = getattr(settings, 'S3_STATIC_FILE_OVERWRITE', True)


class StaticStorage(S3BotoStorage):
    """ S3 Storage for static files """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = S3_STATIC_ROOT
        kwargs['file_overwrite'] = S3_STATIC_FILE_OVERWRITE
        super(StaticStorage, self).__init__(*args, **kwargs)

    def url(self, name):
        url = super(StaticStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url


class MediaStorage(S3BotoStorage):
    """ S3 Storage for uploaded media files """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = S3_MEDIA_ROOT
        kwargs['file_overwrite'] = S3_MEDIA_FILE_OVERWRITE
        super(MediaStorage, self).__init__(*args, **kwargs)
