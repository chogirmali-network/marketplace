import uuid

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    @property
    def class_name(self):
        return self.__class__.__name__

    class Meta:
        abstract = True
        ordering = ('id', )


class S3Attachment(BaseModel):
    url = models.TextField(null=True, blank=True)
    bucket = models.CharField(max_length=500)
    key = models.CharField(max_length=300, unique=True)
    file_id = models.UUIDField(default=uuid.uuid5, editable=False, unique=True)

    def __str__(self):
        return self.url if self.url else self.key

    class Meta:
        db_table = 's3_attachments'


class TelegramStorage(BaseModel):
    PHOTO = 'photo'
    AUDIO = 'audio'
    VIDEO = 'video'
    FILE = 'file'
    DOCUMENT = 'document'

    FILE_TYPES = (
        (PHOTO, 'Photo'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
        (FILE, 'File'),
        (DOCUMENT, 'Document'),
    )

    chat_id = models.BigIntegerField()
    file_type = models.CharField(max_length=30, choices=FILE_TYPES)
    file_id = models.TextField()
    file_unique_id = models.TextField()
    file_size = models.PositiveIntegerField()
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    thumbnail = models.ForeignKey(
        'self', models.SET_NULL, 'thumbnail', null=True, blank=True
    )
    duration = models.PositiveIntegerField(null=True, blank=True)
    performer = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    file_name = models.CharField(max_length=500, null=True, blank=True)
    file_path = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'telegram_storage'
