from django.contrib import admin
from .models import StripeCustomer

@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'stripeCustomerId', 'stripeSubscriptionId')
# admin.site.register(StripeCustomer)