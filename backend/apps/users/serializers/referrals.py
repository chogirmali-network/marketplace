from rest_framework import serializers
from rest_framework.validators import ValidationError

from users.models import Referral, User
from users.serializers.sign_up import SignUpSerializer


class ReferralSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        referral_code = self.context.get('referral_code')
        user = self.context.get('request').user
        if user.is_anonymous:
            serializer = SignUpSerializer(data=self.context.get('request').data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        referral, created = Referral.objects.get_or_create(
            invited_user__referral_code=referral_code,
            logged_in_user=user,
            defaults={
                'invited_user': User.objects.filter(referral_code=referral_code).first()
            }
        )
        if created:
            raise ValidationError({'referral_code': "You already logged in with this referral code!"})
        return referral

    class Meta:
        model = Referral
        fields = (
            'id',
            'invited_user',
            'logged_in_user',
        )
        read_only_fields = (
            'id',
            'invited_user',
            'logged_in_user',
        )
