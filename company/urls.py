from django.urls import path
from .views import CompanyView, EmployeeView

urlpatterns = [
    path('company/<int:company_id>/', CompanyView.as_view(), name='company_retrieve_update_destroy'),
    path('employee/<int:employee_id>/', EmployeeView.as_view(), name='employee_retrieve_update_destroy'),
]
