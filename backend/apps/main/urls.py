from django.urls import path
from main.views import MessageView, NotificationView, UserThemeView, ChatView


urlpatterns = [
    path('message', MessageView.as_view(), name='message'),
    path('chat', ChatView.as_view(), name='chat'),
    path('notification', NotificationView.as_view(), name='notification'),
    path('user-theme', UserThemeView.as_view(), name='user-theme'),
]
