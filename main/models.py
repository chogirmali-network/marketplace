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
    author = models.OneToOneField(User, on_delete=models.CASCADE)
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

class Question(models.Model):
    Quiz = "quiz"
    Multiple = "multiple"
    With_custom_answer = "with_custom_answer"
    Vote = "vote"
    TYPES = (
        (Quiz,"Quiz"),
        (Multiple,"Multiple"),
        (With_custom_answer,"With_custom_answer"),
        (Vote,"Vote")
    )
    question = models.CharField(max_length=255)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30,choices=TYPES, default=Quiz)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
