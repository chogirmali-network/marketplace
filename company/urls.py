from django.urls import path
from company.views import AddCompanyView, AddEmployeeView


urlpatterns = [
    path('add-company', AddCompanyView.as_view(), name='add-company'),
    path('add-employee', AddEmployeeView.as_view(), name='add-employee'),
]
