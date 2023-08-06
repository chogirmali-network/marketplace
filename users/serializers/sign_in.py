from rest_framework import serializers
from django.contrib.auth import authenticate


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, trim_whitespace=True)
    password = serializers.CharField(required=True, trim_whitespace=False)

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get('request'),
            email=attrs.get('email'),
            password=attrs.get('password')
        )

        if not user:
            raise serializers.ValidationError({'password': "Wrong password or email"})

        attrs['user'] = user
        return attrs
