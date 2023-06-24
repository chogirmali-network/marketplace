from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from django.utils.text import slugify


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    object_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Image - {self.image.url}"

    class Meta:
        db_table = 'images'



class Video(models.Model):
    title = models.CharField(max_length=1000)
    caption = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    # frontend usage like this <p>Duration: {{ video.duration|time }}</p>
    video = models.TextField()
    object_id = models.TextField()
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    category = models.ForeignKey('mediafiles.Category', on_delete=models.PROTECT, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Video - {self.video}"

    class Meta:
        db_table = 'videos'


class VideoRanking(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'Video category - {self.title}'

    class Meta:
        db_table = 'video_categories'
        verbose_name_plural = 'Categories'


class Badge(models.Model):
    code = models.CharField(max_length=300)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    logo = models.ImageField(upload_to='badges/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Badge - {self.logo.url}'

    class Meta:
        db_table = 'badges'

