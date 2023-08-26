import uuid

from django.db import models


class S3Attachment(models.Model):
    url = models.TextField(null=True, blank=True)
    bucket = models.CharField(max_length=500)
    key = models.CharField(max_length=300, unique=True)
    file_id = models.UUIDField(default=uuid.uuid5, editable=False, unique=True)

    def __str__(self):
        return self.url if self.url else self.key

    class Meta:
        db_table = 's3_attachments'
