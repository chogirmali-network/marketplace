from rest_framework import serializers
from users.models import User, SubscriptionPlan



class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=2000)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=10000)
    login_type = serializers.CharField(max_length=200)
    subscription_plan = serializers.SerializerMethodField()


    def create(self, data):
        email = data.get('email')
        user = User.objects.filter(email=email).first()
        if not user:
            user = User.objects.create(**data)
            plan = SubscriptionPlan.objects.create(plan=SubscriptionPlan.FREE, user=user, price_monthly=0)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('first_name', instance.email)
        instance.language = validated_data.get('language', instance.language)
        instance.password = validated_data.get('password', instance.password)
        instance.two_step_verification_password = validated_data.get('first_name', instance.two_step_verification_password)
        instance.is_verify_account = validated_data.get('is_verify_account', instance.is_verify_account)
        instance.login_type = validated_data.get('login_type', instance.login_type)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'referral_code', 'language', 'password', 'two_step_verification_password', 'login_type', 'is_verify_account', 'subscription_plan')
        read_only_fields = ('id', )
        extra_kwargs = {
            'password': {'write_only': True},
            'two_step_verification_password': {'write_only': True}
        }

    def get_subscription_plan(self, obj):
        return SubscriptionPlan.objects.get(user=obj).plan
