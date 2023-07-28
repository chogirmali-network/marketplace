from django.urls import path, include
from users.views.users import UserView, PinnedChatView


urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('user/<int:user_id>', UserView.as_view(), name='user-detail'),
    path("pinneds", PinnedChatView.as_view(), name="pinned-list"),
    path("pinned/<int:pinned_id/>", PinnedChatView.as_view(), name="pinned-detail"),
]
