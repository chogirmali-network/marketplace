import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from users.querysets.user import UserManager

from core.models import S3Attachment
from core.utils.langs import SUPPORTED_LANGUAGES
from core.utils.login_types import LOGIN_TYPES


class User(AbstractBaseUser, PermissionsMixin):
    DARK = 'dark'
    LIGHT = 'light'

    DEVELOPER = 'developer'
    CUSTOMER = 'customer'
    COMPANY_REPRESENTATIVE = 'company_representative'

    DEFAULT_THEMES = (
        (DARK, 'Dark'),
        (LIGHT, 'Light')
    )

    USER_ROLES = (
        (DEVELOPER, 'Developer'),
        (CUSTOMER, 'Customer'),
        (COMPANY_REPRESENTATIVE, 'Company representative')
    )

    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000, null=True, blank=True)
    username = models.CharField(max_length=1500, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    profile_image = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, null=True, blank=True, related_name='profile_images')
    cover_image = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, null=True, blank=True, related_name='cover_images')
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    language = models.CharField(max_length=5, choices=SUPPORTED_LANGUAGES, null=True, blank=True)
    referral_code = models.CharField(max_length=20, unique=True)
    invited_code = models.CharField(max_length=20, null=True, blank=True)
    two_step_verification_password = models.TextField(null=True, blank=True)
    is_verify_account = models.BooleanField(default=False)
    login_type = models.CharField(max_length=200, choices=LOGIN_TYPES)
    default_theme = models.CharField(max_length=10, choices=DEFAULT_THEMES, default=LIGHT)
    role = models.CharField(max_length=100, choices=USER_ROLES)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

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
    themes = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)
    price_monthly = models.DecimalField(max_digits=20, decimal_places=2)
    expires_in = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.email + ' - ' + self.plan

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


class Referral(models.Model):
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    logged_in_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_referrals')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.invited_user.email + ' - ' + self.logged_in_user.email

    @property
    def referral_code(self):
        return self.invited_user.referral_code

    class Meta:
        db_table = 'referrals'


class Project(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)    
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'


class Client(models.Model):
    employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_clients')
    client = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_employees')
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


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.team.name

    class Meta:
        db_table = 'team_members'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
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
    account = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f'Wallet of {self.user.email}'

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pinned_chat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'pinned_chats'
