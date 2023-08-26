from rest_framework import serializers

from backend.apps.users.serializers.users import User, SubscriptionPlan
from backend.apps.users.utils.referral_code import generate_referral_code

from backend.apps.core.utils.login_types import EMAIL


class SignUpSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        validated_data['login_type'] = EMAIL
        validated_data['referral_code'] = generate_referral_code()
        user = super().create(validated_data)
        SubscriptionPlan.objects.create(
            user=user,
            price_monthly=0,
            plan=SubscriptionPlan.FREE,
        )
        return user

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
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'login_type': {'read_only': True}
        }
