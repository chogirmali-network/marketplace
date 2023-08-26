from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from users.models import User

from core.models import S3Attachment


class Image(models.Model):
    image = models.ForeignKey(S3Attachment, on_delete=models.PROTECT),
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    size = models.PositiveIntegerField()

    class Meta:
        db_table = 'images'


class Video(models.Model):
    title = models.CharField(max_length=1000)
    caption = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    # frontend usage like this <p>Duration: {{ video.duration|time }}</p>
    size = models.PositiveIntegerField()
    video = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, related_name='videos')
    banner = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, null=True, blank=True, related_name='banners')
    category = models.ForeignKey('mediafiles.Category', on_delete=models.PROTECT, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

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
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video_categories'
        verbose_name_plural = 'Categories'


class Badge(models.Model):
    title = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    badge = models.ForeignKey(S3Attachment, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'badges'
