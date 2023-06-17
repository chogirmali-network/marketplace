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


class Quiz(models.Model):
    Question = "question"
    Multiple = "multiple"
    With_custom_answer = "with_custom_answer"
    Vote = "vote"
    TYPES = (
        (Question, "Question"),
        (Multiple, 'Multiple'),
        (With_custom_answer, 'With_custom_answer'),
        (Vote, 'Vote')
    )
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=TYPES, default=Question)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)
    
    # def __str__(self) -> str:
    #     return self.author
    
    class Meta:
        db_table = 'Quiz'
        
        
class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Answer'