from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Video - {self.video}"

    class Meta:
        db_table = 'videos'

