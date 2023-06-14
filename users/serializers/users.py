from rest_framework.serializers import ModelSerializer
from users.models import User, SubscriptionPlan



class UserSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'referral_code', 'language', 'password', 'two_step_verification_password', 'login_type')
        read_only_fields = ('id', )
        extra_kwargs = {
            'password': {'write_only': True}
        }
