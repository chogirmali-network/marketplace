from django.db import models

from backend.apps.users.models import User

from backend.apps.core.models import S3Attachment


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ForeignKey(S3Attachment, on_delete=models.PROTECT, null=True, blank=True)
    field = models.ForeignKey('company.CompanyField', on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    latitude = models.BigIntegerField(null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=500)
    ceo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='companies')
    info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'Companies'


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'company_fields'
