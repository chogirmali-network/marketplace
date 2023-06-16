from django.db import models
import uuid
from users.models import User,Project,Team
from mediafiles.models import Badge
from company.models import Company
from django.core.validators import MinValueValidator, MaxValueValidator
from mediafiles.models import Badge



      # User.apps

class DeletedUser(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"User - {self.first_name}"

    class Meta:
        db_table = "deleted_users"


class DeletedSubscriptionPlan(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Subscription - {self.user.first_name} to {self.plan}"

    class Meta:
        db_table = 'deleted_subscription_plans'



class DeletedProject(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)    
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Project - {self.name}'

    class Meta:
        db_table = 'deleted_projects'



class DeletedClient(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='deleted_clients')
    client = models.ForeignKey(User,on_delete=models.CASCADE, related_name='deleted_employees')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Client {self.client.first_name} to {self.employee.first_name}'

    class Meta:
        db_table = 'deleted_clients'


class DeletedTeam(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Team - {self.title}'

    class Meta:
        db_table = 'deleted_teams'


class DeletedMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Member {self.user.first_name} of team {self.team.name}'

    class Meta:
        db_table = 'deleted_members'


class DeletedTeamBadge(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Badge {self.badge.logo.url} of team {self.team.name}'

    class Meta:
        db_table = 'deleted_team_badges'


class DeletedUserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Badge {self.badge.logo.url} of user {self.user.first_name}'

    class Meta:
        db_table = 'deleted_user_badges'


class DeletedSavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.first_name} - {self.project.name}"

    class Meta:
        db_table = 'deleted_saved_projects'


class DeletedRankingProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'User {self.user.first_name} ranked to project {self.project.name} with {self.stars} star(s)'

    class Meta:
        db_table = 'deleted_ranking_projects'


   # Mediafiles.apps
class DeletedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    object_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Image - {self.image.url}"

    class Meta:
        db_table = 'deleted_images'



class DeletedVideo(models.Model):
    video = models.TextField()
    object_id = models.TextField()
    # banner = models.ImageField(upload_to='banners/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Video - {self.video}"

    class Meta:
        db_table = 'deleted_videos'


class DeletedBadge(models.Model):
    code = models.CharField(max_length=300)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    logo = models.ImageField(upload_to='badges/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Badge - {self.logo.url}'

    class Meta:
        db_table = 'deleted_badges'






    # main.apps
class DeletedPost(models.Model):
    HTML = 'html'
    MARKDOWN = 'markdown'
    CYBERSELL = 'cybersell'

    PARSE_MODES = (
        (HTML, 'HTML'),
        (MARKDOWN, 'MARKDOWN'),
        (CYBERSELL, 'CYBERSELL')
    )

    content = models.TextField()
    author = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    parse_mode = models.CharField(max_length=20, choices=PARSE_MODES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'Post - {self.content|30}'

    class Meta:
        db_table = 'deleted_posts'


    # company.apps

class DeletedCompany(models.Model):
    IT = 'it'
    ECOMMERCE = 'ecommerce'
    MARKETING_SALES = 'marketing_sales'

    FIELDS = (
        (IT, 'Information Technologies'),
        (ECOMMERCE, 'E-Commerce'),
        (MARKETING_SALES, 'Marketing & Sales')
    )
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logoes/')
    field = models.CharField(max_length=500, choices=FIELDS)
    address = models.TextField(null=True, blank=True)
    latitude = models.BigIntegerField(null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=500)
    ceo = models.OneToOneField(User, on_delete=models.PROTECT)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Company - {self.name}"

    class Meta:
        db_table = 'deleted_companies'
        verbose_name_plural = 'Categories'


class DeletedEmployee(models.Model):
    company = models.ManyToManyField(Company)
    user = models.ManyToManyField(User)
    work_started_at = models.DateTimeField()
    work_ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return f"Employee of {self.company.name}"

    class Meta:
        db_table = 'deleted_employees'
