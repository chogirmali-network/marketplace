from django.db import models

# Create your models here.
class Notifications(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    User = models.CharField(max_length=155,verbose_name='Kimdan..?')
    Content = models.TextField()
    why = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    deleted_time = models.DateTimeField(null=True,blank=True)
    is_view = models.BooleanField()