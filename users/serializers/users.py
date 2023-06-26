from rest_framework.serializers import ModelSerializer
from users.models import *


class UserSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'referral_code', 'language', 'password',
                  'two_step_verification_password', 'login_type')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


class BadgePresentSerializer(ModelSerializer):
    class Meta:
        model = BadgeForPresent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return BadgeForPresent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.badge = validated_data.get('badge', instance.badge)
        instance.from_user = validated_data.get('from_user', instance.from_user)
        instance.to_user = validated_data.get('to_user', instance.to_user)
        instance.save()
        return instance


class MoneyPresentSerializer(ModelSerializer):
    class Meta:
        model = MoneyForPresent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return MoneyForPresent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.from_user = validated_data.get('from_user', instance.from_user)
        instance.to_user = validated_data.get('to_user', instance.to_user)
        instance.save()
        return instance


class VerificationPresentSerializer(ModelSerializer):
    class Meta:
        model = VerificationLabelForPresent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return VerificationLabelForPresent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.from_user = validated_data.get('from_user', instance.from_user)
        instance.to_user = validated_data.get('to_user', instance.to_user)
        instance.save()
        return instance


class SubscriptionPlanPresentSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionPlanForPresent
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return SubscriptionPlanForPresent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sub_plan = validated_data.get('sub_plan', instance.sub_plan)
        instance.from_user = validated_data.get('from_user', instance.from_user)
        instance.to_user = validated_data.get('to_user', instance.to_user)
        instance.save()
        return instance
