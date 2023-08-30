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

class Service(models.Model):
    title = models.CharField(max_length=250)
    services = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attachment = models.ForeignKey(S3Attachment, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'service'