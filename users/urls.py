from django.urls import path, include
from users.views import UserCreateView


urlpatterns = [
    path('user/', include([
        path('create/', UserCreateView.as_view(), name='user-create'),
    ]))
]

