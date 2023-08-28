from django.urls import path
from mediafiles.views import VideoView


urlpatterns = [
    path('videos', VideoView.as_view(), name='videos'),
    path('video/<int:video_id>', VideoView.as_view(), name='video-detail'),
]
