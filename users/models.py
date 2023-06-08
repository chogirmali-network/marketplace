import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    UZ = 'uz'
    EN = 'en'
    RU = 'ru'

    LANGUAGES = (
        (UZ, 'Uz'),
        (EN, 'En'),
        (RU, 'Ru')
    )

    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField(unique=True)
    token = models.TextField()
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    language = models.CharField(max_length=5, choices=LANGUAGES, null=True, blank=True)
    referral_code = models.CharField(max_length=20, null=True, blank=True)
    password = models.TextField()
    two_step_verification_password = models.TextField()


    def __str__(self) -> str:
        return f"User - {self.first_name}"

    class Meta:
        db_table = "users"


class SubscriptionPlan(models.Model):
    FREE = 'free'
    CUSTOM = 'custom'

    PLANS = (
        (FREE, 'Free'),
        (CUSTOM, 'Custom')
    )

    plan = models.CharField(max_length=1000, default=FREE, choices=PLANS)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload_projects = models.PositiveBigIntegerField(validators=[MinValueValidator(6), MaxValueValidator(1000)], default=5)
    write_blog = models.PositiveBigIntegerField(validators=[MinValueValidator(4), MaxValueValidator(1000)], default=3)
    join_team = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)
    get_badges = models.PositiveBigIntegerField(validators=[MinValueValidator(4), MaxValueValidator(1000)], default=3)
    themes = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)


    def __str__(self) -> str:
        return f"Subscription - {self.user.first_name} to {self.plan}"

    class Meta:
        db_table = 'subscription_plans'


