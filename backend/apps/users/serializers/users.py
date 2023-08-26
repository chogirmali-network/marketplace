from rest_framework import serializers

from backend.apps.users.serializers.users import User, SubscriptionPlan, PinnedChat


class UserSerializer(serializers.ModelSerializer):
    subscription_plan = serializers.SerializerMethodField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def get_subscription_plan(self, obj):
        serializer = SubscriptionPlanSerializer(SubscriptionPlan.objects.get(user=obj))
        return serializer.data

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'profile_image',
            'cover_image',
            'language',
            'login_type',
            'default_theme',
            'referral_code',
            'password',
            'subscription_plan',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'login_type': {'read_only': True},
            'referral_code': {'read_only': True},
        }


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = (
            'id',
            'plan',
            'upload_projects',
            'themes',
            'price_monthly',
            'expires_in',
        )


class PinnedChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinnedChat
        fields = (
            'id',
            'chat_id',
            'user',
        )
