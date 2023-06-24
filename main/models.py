from django.db import models
from users.models import User


class Message(models.Model):
    HTML = 'html'
    MARKDOWN = 'markdown'
    CYBERSELL = 'cybersell'

    PARSE_MODES = (
        (HTML, 'HTML'),
        (MARKDOWN, 'MARKDOWN'),
        (CYBERSELL, 'CYBERSELL')
    )

    content = models.TextField()
    object_id = models.TextField()
    parse_mode = models.CharField(max_length=20, choices=PARSE_MODES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Post - {self.content|30}'

    class Meta:
        db_table = 'posts'


class Notification(models.Model):
    object_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_view = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Notification from {self.object_id} to {self.user.first_name}'

    class Meta:
        db_table = 'notifications'



class Theme(models.Model):
    name = models.CharField(max_length=300)
    link = models.TextField()  # link to theme file as json
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Theme - {self.name}"

    class Meta:
        db_table = 'themes'


class UserTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Theme {self.theme.name} for user {self.user.first_name}"
