from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.models import Message
from main.serializers import MessageSerializer



class MessageView(APIView):
    def get(self, request, message_id=None):
        if message_id:
            message = get_object_or_404(Message, id=message_id)
            serializer = MessageSerializer(instance=message)
        else:
            messages = Message.objects.all()
            serializer = MessageSerializer(instance=messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, message_id):
        instance = get_object_or_404(Message, id=message_id)
        serializer = MessageSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, message_id):
        message = get_object_or_404(Message, id=message_id)
        message.deleted_at = timezone.now()
        message.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

