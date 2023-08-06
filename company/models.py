from django.db import models
from users.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logoes/')
    field = models.ForeignKey('company.CompanyField', on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    latitude = models.BigIntegerField(null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=500)
    ceo = models.OneToOneField(User, on_delete=models.PROTECT)
    info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'Companies'


class Employee(models.Model):
    company = models.ManyToManyField(Company)
    user = models.ManyToManyField(User)
    work_started_at = models.DateTimeField(null=True, blank=True)
    work_ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.company.name

    class Meta:
        db_table = 'employees'


class CompanyField(models.Model):
    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'company_fields'
