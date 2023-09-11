from rest_framework import serializers
from main.models import Message, Notification, UserTheme, Chat, Theme


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'id',
            'content',
            'chat_id',
            'parse_mode',
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


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = (
            'id',
            'title',
            'type'
        )


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'link'
        )
