from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.logo = validated_data.get("logo", instance.logo)
        instance.field = validated_data.get("field", instance.field)
        instance.address = validated_data.get("address", instance.address)
        instance.latitude = validated_data.get("latitude", instance.latitude)
        instance.longitude = validated_data.get("longitude", instance.longitude)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.ceo = validated_data.get("ceo", instance.ceo)
        instance.info = validated_data.get("info", instance.info)
        instance.deleted_at = validated_data.get("deleted_at", instance.deleted_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
        )

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.company = validated_data.get("company", instance.company)
        instance.user = validated_data.get("user", instance.user)
        instance.work_started_at = validated_data.get(
            "work_started_at", instance.work_started_at
        )
        instance.work_ended_at = validated_data.get(
            "work_ended_at", instance.work_ended_at
        )
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.deleted_at = validated_data.get("deleted_at", instance.deleted_at)
        instance.save()
        return instance
