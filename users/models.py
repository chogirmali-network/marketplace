import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from mediafiles.models import Badge

class User(models.Model):
    GITHUB = 'github'
    LINKEDIN = 'linkedin'
    GOOGLE = 'google'
    EMAIL = 'email'

    UZ = 'uz'
    EN = 'en'
    RU = 'ru'

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

    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000, null=True, blank=True)
    email = models.EmailField(unique=True)
    token = models.TextField()
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    language = models.CharField(max_length=5, choices=LANGUAGES, null=True, blank=True)
    referral_code = models.CharField(max_length=20, null=True, blank=True)
    password = models.TextField()
    two_step_verification_password = models.TextField(null=True, blank=True)
    is_verify_account = models.BooleanField(default=False)
    login_type = models.CharField(max_length=200, choices=LOGIN_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"User - {self.first_name}"

    def get_subscription_plan(self):
        return SubscriptionPlan.objects.get(user=self).plan

    def make_verify_account(self):
        if self.is_verify_account == False:
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload_projects = models.PositiveBigIntegerField(validators=[MinValueValidator(6), MaxValueValidator(1000)], default=5)
    write_blog = models.PositiveBigIntegerField(validators=[MinValueValidator(4), MaxValueValidator(1000)], default=3)
    join_team = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)
    get_badges = models.PositiveBigIntegerField(validators=[MinValueValidator(4), MaxValueValidator(1000)], default=3)
    themes = models.PositiveBigIntegerField(validators=[MinValueValidator(3), MaxValueValidator(1000)], default=2)
    price_monthly = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Subscription - {self.user.first_name} to {self.plan.title()} for {self.price_monthly if self.price_monthly else '0'} $"

    class Meta:
        db_table = 'subscription_plans'



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
    employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='client')
    client = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Client {self.client.first_name} to {self.employee.first_name}'

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
        return f'Team - {self.name}'

    class Meta:
        db_table = 'teams'


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Member {self.user.first_name} of team {self.team.name}'

    class Meta:
        db_table = 'members'


class TeamBadge(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f'Badge {self.badge.logo.url} of team {self.team.name}'

    class Meta:
        db_table = 'team_badges'


class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
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


    def __str__(self) -> str:
        return f'User {self.user.first_name} bought a project {self.project.name}'

    class Meta:
        db_table = 'sold_projects'
