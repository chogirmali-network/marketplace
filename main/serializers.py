from rest_framework import serializers
from main.models import Message, Notification, UserTheme


class MessageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.parse_mode = validated_data.get('parse_mode', instance.parse_mode)
        instance.save()
        return instance

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

    def create(self, validated_data):
        return super().create(validated_data)

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

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = UserTheme
        fields = (
            'id',
            'theme',
            'user',
        )
