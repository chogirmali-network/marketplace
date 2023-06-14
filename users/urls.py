from django.urls import path, include
from users.views import UserCreateView, UserDetailView


urlpatterns = [
    path('user/', include([
        path('detail/<int:user_id>', UserDetailView.as_view(), name='user-detail'),
        path('create/', UserCreateView.as_view(), name='user-create'),
    ]))
]

