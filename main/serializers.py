from rest_framework import serializers
from main.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', 'object_id', 'parse_mode', 'updated_at', 'deleted_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.parse_mode = validated_data.get('parse_mode', instance.parse_mode)
        instance.save()
        return instance
