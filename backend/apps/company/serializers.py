from rest_framework import serializers
from company.models import Company, Employee, CompanyField


class AddCompanySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'phone_number',
            'ceo',
            'logo',
            'field',
            'info',
            'latitude',
            'longitude',
            'address',
        )


class AddEmployeeSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Employee
        fields = (
            'id',
            'company',
            'user',
            'work_started_at',
            'work_ended_at',
        )


class AddCompanyFieldSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = CompanyField
        fields = (
            'id',
            'title',
            'work_started_at',
            'work_ended_at',
        )
