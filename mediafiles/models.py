from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    object_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Image - {self.image.url}"

    class Meta:
        db_table = 'images'



class Video(models.Model):
    video = models.TextField()
    object_id = models.TextField()
    # banner = models.ImageField(upload_to='banners/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Video - {self.video}"

    class Meta:
        db_table = 'videos'


class Badge(models.Model):
    code = models.CharField(max_length=300)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    logo = models.ImageField(upload_to='badges/')


    def __str__(self) -> str:
        return f'Badge - {self.logo.url}'

    class Meta:
        db_table = 'badges'

