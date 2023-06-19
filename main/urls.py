from django.urls import path
from main.views import MessageView


urlpatterns = [
    path('messages', MessageView.as_view(), name='messages'),
    path('message/<int:message_id>', MessageView.as_view(), name='message-detail'),
]

