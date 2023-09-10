from rest_framework import serializers
from main.models import Message, Notification, UserTheme, Chat, Theme


class MessageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Message
        fields = (
            'id',
            'content',
            'chat_id',
            'parse_mode',
        )


class NotificationSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

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

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = UserTheme
        fields = (
            'id',
            'theme',
            'user',
        )


class ChatSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Chat
        fields = (
            'id',
            'title',
            'type'
        )


class ThemeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'link'
        )
