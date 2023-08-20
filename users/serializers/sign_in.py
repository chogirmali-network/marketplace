from rest_framework import serializers

from users.models import User


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, trim_whitespace=True)
    password = serializers.CharField(required=True, trim_whitespace=False)

    def validate(self, attrs):
        user = User.objects.filter(
            email=attrs.get('email'),
            password=attrs.get('password')
        ).first()

        if not user:
            raise serializers.ValidationError({'password': "Wrong password or email"})

        attrs['user'] = user
        return attrs
