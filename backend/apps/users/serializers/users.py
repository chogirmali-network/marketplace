from rest_framework import serializers

from users.models import User, SubscriptionPlan, PinnedChat, UserService, Service, BannedUser, Device, Wallet, \
    SoldProject, RankingProject, SavedProject, TeamBadge, TeamMember, Client, Team, ProjectData, Project, ExtraLink


class UserSerializer(serializers.ModelSerializer):
    subscription_plan = serializers.SerializerMethodField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def get_subscription_plan(self, obj):
        serializer = SubscriptionPlanSerializer(SubscriptionPlan.objects.get(user=obj))
        return serializer.data

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'profile_image',
            'cover_image',
            'language',
            'login_type',
            'default_theme',
            'referral_code',
            'password',
            'subscription_plan',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'login_type': {'read_only': True},
            'referral_code': {'read_only': True},
        }


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = (
            'id',
            'plan',
            'upload_projects',
            'themes',
            'price_monthly',
            'expires_in',
        )


class PinnedChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinnedChat
        fields = (
            'id',
            'chat_id',
            'user',
        )


class ExtraLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraLink
        fields = (
            'id',
            'user',
            'link',
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'price',
            'author',
            'image',
            'is_active',
        )


class ProjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectData
        fields = (
            'id',
            'provider',
            'project',
            'data',
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'employee',
            'client',
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'owner',
            'logo',
        )


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = (
            'id',
            'team',
            'user',
        )


class TeamBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamBadge
        fields = (
            'id',
            'team',
            'badge',
        )


class SavedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProject
        fields = (
            'id',
            'team',
            'project',
        )


class RankingProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingProject
        fields = (
            'id',
            'project',
            'user',
            'stars',
        )


class SoldProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProject
        fields = (
            'id',
            'project',
            'user',
        )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            'id',
            'user',
            'account',
        )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'id',
            'ip_address',
            'user',
        )


class BannedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedUser
        fields = (
            'id',
            'user',
            'revision',
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'title',
            'code',
            'price',
            'attachment',
            'description',
            'is_active',
        )


class UserServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserService
        fields = (
            'id',
            'service',
            'user',
            'expires_in',
            'is_active',
        )
