from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'proverse'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
