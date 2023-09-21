from django.contrib import admin
from .models import Company, Employee, CompanyField


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'field', 'address', 'ceo', )
  fields = ('id', 'name', 'logo', 'field', 'address', 'latitude', 'longitude', 'phone_number', 'ceo', 'info', )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('id', 'company', 'user', 'work_started_at', 'work_ended_at', )
  fields = ('id', 'company', 'user', 'work_started_at', 'work_ended_at', )


@admin.register(CompanyField)
class CompanyFieldAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', )
  fields = ('id', 'title', )
