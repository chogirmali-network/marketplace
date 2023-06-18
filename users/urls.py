from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', VideoLessonCreateDetailUpdateDelete.as_view(), name='index'),
    path('', VideoLessonCreateDetailUpdateDelete.as_view(), name='index'),
    path('video_category/<int:pk>/', VideoCategoriesCreateDetailUpdateDelete.as_view(),
         name='video_category'),
    path('video_category/', VideoCategoriesCreateDetailUpdateDelete.as_view(), name='video_categories'),
    path('category/<int:pk>/', CategoryCreateDetailUpdateDelete.as_view(), name='categories'),
    path('category/', CategoryCreateDetailUpdateDelete.as_view(), name='category'),
    path('message/<int:pk>', MessagesCreateDetailUpdateDelete.as_view(), name='message'),
    path('message/', MessagesCreateDetailUpdateDelete.as_view(), name='messages'),
    path('chat/<int:pk>', ChatsCreateDetailUpdateDelete.as_view(), name='chat'),
    path('chat/', ChatsCreateDetailUpdateDelete.as_view(), name='chats'),

]
