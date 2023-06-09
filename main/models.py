from django.db import models
from users.models import User


class Post(models.Model):
    HTML = 'html'
    MARKDOWN = 'markdown'
    CYBERSELL = 'cybersell'

    PARSE_MODES = (
        (HTML, 'HTML'),
        (MARKDOWN, 'MARKDOWN'),
        (CYBERSELL, 'CYBERSELL')
    )

    content = models.TextField()
    author = models.OneToOneField(User, on_delete=models.SET_NULL)
    parse_mode = models.CharField(max_length=20, choices=PARSE_MODES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Post - {self.content|30}'

    class Meta:
        db_table = 'posts'

