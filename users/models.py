import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.querysets.user import UserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    GITHUB = 'github'
    LINKEDIN = 'linkedin'
    GOOGLE = 'google'
    EMAIL = 'email'

    UZ = 'uz'
    EN = 'en'
    RU = 'ru'

    DARK = 'dark'
    LIGHT = 'light'

    LANGUAGES = (
        (UZ, 'Uz'),
        (EN, 'En'),
        (RU, 'Ru')
    )

    LOGIN_TYPES = (
        (GITHUB, 'Github'),
        (GOOGLE, 'Google'),
        (LINKEDIN, 'Linkedin'),
        (EMAIL, 'Email')
    )

    DEFAULT_THEMES = (
        (DARK, 'Dark'),
        (LIGHT, 'Light')
    )

    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000, null=True, blank=True)
    username = models.CharField(max_length=1500, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    profile_image = models.TextField(null=True, blank=True)
    cover_image = models.TextField(null=True, blank=True)
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    language = models.CharField(max_length=5, choices=LANGUAGES, null=True, blank=True, default=EN)
    referral_code = models.CharField(max_length=20, null=True, blank=True)
    two_step_verification_password = models.TextField(null=True, blank=True)
    is_verify_account = models.BooleanField(default=False)
    login_type = models.CharField(max_length=200, choices=LOGIN_TYPES)
    default_theme = models.CharField(max_length=10, choices=DEFAULT_THEMES, default=LIGHT)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.email

    def get_subscription_plan(self):
        return self.subscription_plan.plan

    def make_verify_account(self):
        if not self.is_verify_account:
            self.is_verify_account = True
            self.save()

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription_plan')
    upload_projects = models.PositiveBigIntegerField(validators=[MinValueValidator(11), MaxValueValidator(1000)], default=10)
    write_blog = models.PositiveBigIntegerField(validators=[MinValueValidator(21), MaxValueValidator(1000)], default=20)
    join_team = models.PositiveBigIntegerField(validators=[MinValueValidator(11), MaxValueValidator(1000)], default=10)
    get_badges = models.PositiveBigIntegerField(validators=[MinValueValidator(16), MaxValueValidator(1000)], default=15)
    themes = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)
    price_monthly = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.plan

    class Meta:
        db_table = 'subscription_plans'


class ExtraLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='extra_links')
    link = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.link}"

    class Meta:
        db_table = 'extra_links'
        unique_together = ('user', 'link')


class Project(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)    
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f'Project - {self.name}'

    class Meta:
        db_table = 'projects'


class Client(models.Model):
    employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_client')
    client = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.client.first_name

    class Meta:
        db_table = 'clients'


class Team(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.team.name

    class Meta:
        db_table = 'members'


class TeamBadge(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    badge = models.ForeignKey('mediafiles.Badge', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.badge.logo.url

    class Meta:
        db_table = 'team_badges'


class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey('mediafiles.Badge', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Badge {self.badge.logo.url} of user {self.user.first_name}'

    class Meta:
        db_table = 'user_badges'


class SavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.user.first_name} - {self.project.name}"

    class Meta:
        db_table = 'saved_projects'


class RankingProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'User {self.user.first_name} ranked to project {self.project.name} with {self.stars} star(s)'

    class Meta:
        db_table = 'ranking_projects'


class SoldProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'User {self.user.first_name} bought a project {self.project.name}'

    class Meta:
        db_table = 'sold_projects'


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Wallet of {self.user.first_name}'

    class Meta:
        db_table = 'wallets'



class Device(models.Model):
    ip_address = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.ip_address} device of {self.user.first_name}"

    class Meta:
        db_table = 'devices'


class BannedUser(models.Model):
    # we should write REVISIONS choices for revision to banning a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    revision = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Banned user {self.user.first_name}"

    class Meta:
        db_table = 'banned_users'


class PinnedChat(models.Model):
    chat_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pinnedchat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'pinned_chat'
