from django.db import models

from users.models import User

from core.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ForeignKey('core.TelegramStorage', on_delete=models.PROTECT, null=True, blank=True)
    field = models.ForeignKey('company.CompanyField', on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    latitude = models.BigIntegerField(null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=500)
    ceo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='companies')
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'Companies'


class Employee(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_started_at = models.DateTimeField(null=True, blank=True)
    work_ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} ({self.company.name})"

    class Meta:
        db_table = 'employees'


class CompanyField(BaseModel):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'company_fields'
