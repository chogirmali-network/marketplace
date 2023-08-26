from django.db import models

from backend.apps.users.models import User

from backend.apps.core.models import S3Attachment


class Message(models.Model):
    HTML = 'html'
    MARKDOWN = 'markdown'

    PARSE_MODES = (
        (HTML, 'HTML'),
        (MARKDOWN, 'MARKDOWN'),
    )

    content = models.TextField()
    chat_id = models.TextField()
    parse_mode = models.CharField(max_length=20, choices=PARSE_MODES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'messages'


class Notification(models.Model):
    chat_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_view = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'notifications'


class Theme(models.Model):
    name = models.CharField(max_length=300)
    link = models.ForeignKey(S3Attachment, on_delete=models.PROTECT)  # link to theme file as json
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'themes'


class UserTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.theme.name
