from rest_framework import serializers
from users.models import PinnedChat

class PinnedChatserializer(serializers.Serializer):
    class Meta:
        model = PinnedChat
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.chat_id = validated_data.get("chat_id", instance.chat_id)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance
    