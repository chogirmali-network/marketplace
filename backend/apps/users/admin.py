from django.contrib import admin

from .models import User, SubscriptionPlan, Project, Client, Team, TeamMember, TeamBadge, UserBadge, \
    SavedProject, RankingProject, SoldProject, Wallet, Referral, Service, UserService, Pricing, MoneyPresent, \
    BadgePresent, VerificationLabelPresent, SubscriptionPlanPresent, SubscriptionPlanPricing


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'is_verify_account', 'is_active', )
    fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone_number', 'is_verify_account',
              'profile_image', 'cover_image', 'language', 'referral_code', 'login_type', 'default_theme', 'is_active', )
    write_only_fields = ('password', )


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'user', 'price_monthly', 'expires_in', 'is_active', )
    fields = ('plan', 'user', 'upload_projects', 'themes', 'price_monthly', 'expires_in', 'is_active', )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'author', )
    fields = ('name', 'description', 'price', 'author', 'image', )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'client', )
    fields = ('employee', 'client', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'description', )
    fields = ('name', 'owner', 'description', )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'user', )
    fields = ('team', 'user', )


@admin.register(TeamBadge)
class TeamBadgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'badge', )
    fields = ('team', 'badge', )


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'badge',)
    fields = ('user', 'badge',)


@admin.register(SavedProject)
class SavedProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', )
    fields = ('user', 'project', )


@admin.register(RankingProject)
class RankingProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'stars', )
    fields = ('user', 'project', 'stars', )


@admin.register(SoldProject)
class SoldProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', )
    fields = ('user', 'project', )


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'account', 'is_active', )
    fields = ('user', 'account', 'is_active', )


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id', 'invited_user', 'logged_in_user', 'referral_code', )
    fields = ('invited_user', 'logged_in_user', 'referral_code', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code', 'price', 'is_active', 'active_users', )
    fields = ('title', 'code', 'price', 'attachment', 'description', 'is_active', )


@admin.register(UserService)
class UserServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'user', 'expires_in', 'is_active', )
    fields = ('service', 'user', 'expires_in', 'is_active', )


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'price', )
    fields = ('code', 'price', )


@admin.register(MoneyPresent)
class MoneyPresentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'amount', 'status', )
    fields = ('from_user', 'to_user', 'amount', 'status', )


@admin.register(BadgePresent)
class BadgePresentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'badge', )
    fields = ('from_user', 'to_user', 'badge', )


@admin.register(VerificationLabelPresent)
class VerificationLabelPresentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', )
    fields = ('from_user', 'to_user', )


@admin.register(SubscriptionPlanPresent)
class SubscriptionPlanPresentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'subscription_plan_data', 'price', 'period', )
    fields = ('from_user', 'to_user', 'subscription_plan_data', 'price', 'period', )


@admin.register(SubscriptionPlanPricing)
class SubscriptionPlanPricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'pricing', 'quotas', )
    fields = ('plan', 'pricing', )
