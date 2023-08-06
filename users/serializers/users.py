from rest_framework import serializers
from users.models import User, SubscriptionPlan, PinnedChat


class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['subscription_plan'] = instance.get_subscription_plan()
        return data

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'referral_code', 'language',
            'login_type', 'is_verify_account', 'subscription_plan', 'default_theme',
        )
        extra_kwargs = {
            'login_type': {'read_only': True},
            'referral_code': {'read_only': True},
        }


class PinnedChatserializer(serializers.Serializer):
    class Meta:
        model = PinnedChat
        fields = ["chat_id", "user"]
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.chat_id = validated_data.get("chat_id", instance.chat_id)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance
