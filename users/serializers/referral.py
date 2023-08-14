from rest_framework import serializers
from users.models import Referral


class ReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = "__all__"
        read_onliy_fields = ("id", "created_at")

    def create(self, validated_data):
        return super().create(validated_data)
