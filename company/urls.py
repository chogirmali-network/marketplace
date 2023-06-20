from django.urls import path
from company.views import CompanyView, EmployeeView


urlpatterns = [
    path('companies', CompanyView.as_view(), name='companies-list'),
    path('company/<int:company_id>', CompanyView.as_view(), name='company-detail'),
    path('employees', EmployeeView.as_view(), name='employees-list'),
    path('employee/<int:employee_id>', EmployeeView.as_view(), name='employee-detail'),
]
