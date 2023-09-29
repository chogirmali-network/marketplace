from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel



class ChatGPT(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.TextField()
    content = models.TextField()
    role = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)