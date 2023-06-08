from django.urls import path
from users.views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-create')
]

