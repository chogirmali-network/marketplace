from django.shortcuts import get_object_or_404
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User


class VideoLessonsModel(models.Model):
    name = models.CharField(max_length=128)
    caption = models.TextField(max_length=1024)
    video = models.TextField()
    duration = models.DurationField(null=True, blank=True)
    # frontend usage like this <p>Duration: {{ video.duration|time }}</p>
    upload_date = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, models.CASCADE)
    course_cost = models.PositiveIntegerField(validators=[MaxValueValidator(1000000)])  # so'mda, max summa 1 mln 1 so'm
    discount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.author} - {self.name}"


class VideoLessonsRating(models.Model):  # ongoing...
    video_lesson = models.ForeignKey(VideoLessonsModel, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=3, decimal_places=2)


# view counts larni ham yasash kerak ammo buning uchun menimcha birinchi api yaratamiz

class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class VideoCategories(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    video = models.ForeignKey(VideoLessonsModel, models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.video}"


class Chats(models.Model):
    sender = models.ForeignKey(User, models.CASCADE, related_name='chat_sender')
    receiver = models.ForeignKey(User, models.CASCADE, related_name='chat_receiver')


class Messages(models.Model):  # ongoing... : image, video sending in next versions
    message = models.TextField()  # text field just for now
    chat = models.ForeignKey(Chats, models.CASCADE)
    send_time = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    seen_time = models.DateTimeField(blank=True, null=True)  # seen time must send only once
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk:
            mess = get_object_or_404(Messages, pk=self.pk)
            if mess.seen_time:
                self.seen_time = mess.seen_time
            self.is_seen = True
        super(Messages, self).save(*args, **kwargs)
