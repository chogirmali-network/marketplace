from django.urls import path, include
from users.views import UserView


urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('user/<int:user_id>', UserView.as_view(), name='user-detail'),
]
