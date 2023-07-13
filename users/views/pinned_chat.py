from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from serializers.pinned_chat import PinnedChatserializer
from users.models import PinnedChat


class PinnedChatView(APIView):
    def get(self, request, pinned_id=None):
        if pinned_id:
            pinned = get_object_or_404(PinnedChat, id=pinned_id)
            serializer = PinnedChatserializer(instance=pinned)
        else:
            pinneds = PinnedChat.objects.all()
            serializer = PinnedChatserializer(instance=pinneds, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requset):
        serializer = PinnedChatserializer(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, pinned_id):
        pinned = get_object_or_404(PinnedChat, id=pinned_id)
        data = request.data
        serializer = PinnedChatserializer(instance=pinned, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)
    
    def delete(self, request, pinned_id):
        pinned = PinnedChat.objects.get(id=pinned_id)
        pinned.deleted_at = timezone.now()
        pinned.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    