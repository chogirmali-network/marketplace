from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from users.serializers.users import UserSerializer
from users.models import User, SubscriptionPlan, PinnedChat
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"

class UserView(views.APIView):
    def get(self, request, user_id=None):
        if user_id:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(instance=user)
        else:
            users = User.objects.all()
            serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, user_id):
        instance = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.deleted_at = timezone.now()
        user.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


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
