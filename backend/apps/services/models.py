from django.db import models

from core.models import BaseModel
from users.models import User


class ChatGPT(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.TextField()
    content = models.TextField()
    role = models.CharField(max_length=20)
