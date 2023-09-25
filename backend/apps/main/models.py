from django.db import models

from users.models import User

from core.models import BaseModel


class Chat(BaseModel):
    GROUP = 'group'
    PRIVATE = 'private'

    TYPES = (
        (GROUP, 'Group'),
        (PRIVATE, 'Private'),
    )
    title = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPES)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_to_user')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'chats'


class Message(BaseModel):
    HTML = 'html'
    MARKDOWN = 'markdown'

    PARSE_MODES = (
        (HTML, 'HTML'),
        (MARKDOWN, 'MARKDOWN'),
    )

    content = models.TextField()
    chat = models.ForeignKey('main.Chat', models.CASCADE, 'messages')
    parse_mode = models.CharField(max_length=20, choices=PARSE_MODES, null=True, blank=True)

    class Meta:
        db_table = 'messages'


class Notification(BaseModel):
    chat = models.ForeignKey('main.Chat', models.CASCADE, 'notifications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_view = models.BooleanField(default=False)

    class Meta:
        db_table = 'notifications'


class Theme(BaseModel):
    name = models.CharField(max_length=300)
    link = models.ForeignKey('core.TelegramStorage', on_delete=models.PROTECT)  # link to theme file as json

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'themes'


class UserTheme(BaseModel):
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme.name
