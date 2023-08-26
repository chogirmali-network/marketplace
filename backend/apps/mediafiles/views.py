from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from backend.apps.mediafiles.models import Video
from backend.apps.mediafiles.serializers import VideoSerializer



class VideoView(APIView):
    def get(self, request, video_id=None):
        if video_id:
            video = get_object_or_404(Video, id=video_id)
            serializer = VideoSerializer(instance=video)
        else:
            videos = Video.objects.all()
            serializer = VideoSerializer(instance=videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, video_id):
        instance = get_object_or_404(Video, id=video_id)
        serializer = VideoSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)
        video.deleted_at = timezone.now()
        video.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


