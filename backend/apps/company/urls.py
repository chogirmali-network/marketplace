from django.urls import path
from backend.apps.company.views import AddCompanyView, AddEmployeeView


urlpatterns = [
    path('add-company', AddCompanyView.as_view(), name='add-company'),
    path('add-employee', AddEmployeeView.as_view(), name='add-employee'),
]
