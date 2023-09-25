from rest_framework import serializers
from main.models import Message, Notification, UserTheme,Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'content',
            'chat_id',
            'parse_mode',
        )


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'id',
            'title',
            'type',
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id',
            'chat_id',
            'user',
            'content',
            'is_view',
        )


class UserThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTheme
        fields = (
            'id',
            'theme',
            'user',
        )
