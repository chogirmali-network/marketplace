from django.contrib import admin
from .models import User as CustomUser, SubscriptionPlan


admin.site.register(CustomUser)
admin.site.register(SubscriptionPlan)