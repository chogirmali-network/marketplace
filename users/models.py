import uuid
from django.shortcuts import get_object_or_404
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
    upload_projects = models.PositiveBigIntegerField(validators=[MinValueValidator(6), MaxValueValidator(1000)],
                                                     default=5)
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


# TICKET-13

class MoneyForPresent(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)  # 1 000 000.00
    from_user = models.ForeignKey(User, models.CASCADE, related_name='from_user_money')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='to_user_money')
    is_succeed = models.BooleanField(default=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            transaction_1 = get_object_or_404(Wallet, user_id=self.from_user)
            transaction_2 = get_object_or_404(Wallet, user_id=self.to_user)
            transaction_1.account = float(transaction_1.account)
            transaction_2.account = float(transaction_2.account)
            amount = float(self.amount)
            if transaction_1.account >= amount:
                transaction_1.account -= amount
                transaction_1.save()
                transaction_2.account += amount
                transaction_2.save()
            else:
                self.is_succeed = False
                # error: transactor's account is not enough for transaction
            super(MoneyForPresent, self).save(*args, **kwargs)

    def __str__(self):
        return f"Money present transaction from '{self.from_user}' to '{self.to_user}' - {self.amount} sum"


class BadgeForPresent(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, models.CASCADE, related_name='from_user_badge')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='to_user_badge')

    def save(self, *args, **kwargs):
        data = {"user": self.to_user, "badge": self.badge}
        # I didn't checked if there same badge existed for same user or not. Which can be trouble as conflict
        UserBadge.objects.create(**data)
        super(BadgeForPresent, self).save(*args, **kwargs)

    def __str__(self):
        return f"Badge ({self.badge}) gifted from {self.from_user} to {self.to_user}"


class VerificationLabelForPresent(models.Model):
    from_user = models.ForeignKey(User, models.CASCADE, related_name='verification_from_user')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='verification_to_user')

    def save(self, *args, **kwargs):
        if not self.pk:
            user = get_object_or_404(User, pk=self.to_user.pk)
            user.make_verify_account()
            super(VerificationLabelForPresent, self).save(*args, **kwargs)

    def __str__(self):
        return f"Verification gifted from {self.from_user} to {self.to_user}"


class SubscriptionPlanForPresent(models.Model):
    sub_plan = models.ForeignKey(SubscriptionPlan, models.CASCADE)
    from_user = models.ForeignKey(User, models.CASCADE, related_name='from_user_sub_plan')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='to_user_sub_plan')

    def __str__(self):
        return f"Subscription plan ({self.sub_plan}) gifted from {self.from_user} to {self.to_user}"
