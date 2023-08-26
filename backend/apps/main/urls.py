from django.urls import path
from backend.apps.main.views import MessageView, NotificationView, UserThemeView


urlpatterns = [
    path('message', MessageView.as_view(), name='message'),
    path('notification', NotificationView.as_view(), name='notification'),
    path('user-theme', UserThemeView.as_view(), name='user-theme'),
]
