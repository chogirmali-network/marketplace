from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.models import UserTheme
from main.serializers import MessageSerializer, NotificationSerializer, UserThemeSerializer, ChatSerializer


class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request):
        serializer = MessageSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class ChatView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request):
        serializer = ChatSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class NotificationView(APIView):
    def post(self, request):
        serializer = NotificationSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request):
        serializer = NotificationSerializer(request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UserThemeView(APIView):
    def get(self, request):
        themes = UserTheme.objects.filter(user=request.user)
        serializer = UserThemeSerializer(themes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = UserThemeSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
