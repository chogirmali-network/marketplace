from rest_framework import serializers
from users.models import User, SubscriptionPlan


class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['login_type'] = User.EMAIL
        user = User.objects.create(**validated_data)
        SubscriptionPlan.objects.create(user=user, price_monthly=0)
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
