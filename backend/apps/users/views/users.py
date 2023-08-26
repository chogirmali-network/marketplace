from django.utils import timezone

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.apps.users.views.users import UserSerializer, PinnedChatSerializer
from backend.apps.users.views.users import PinnedChat


class UserDetailView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data, status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        request.user.deleted_at = timezone.now()
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PinnedChatView(APIView):
    def get(self, request):
        pinned_chats = PinnedChat.objects.filter(user=request.user, deleted_at__isnull=True)
        serializer = PinnedChatSerializer(pinned_chats, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = PinnedChatSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
