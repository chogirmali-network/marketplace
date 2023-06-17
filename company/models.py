from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
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
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) -> str:
        return f"Company - {self.name}"

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
        return f"Employee of {self.company.name}"

    class Meta:
        db_table = 'employees'

