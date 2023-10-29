from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=250)
    current_period_end = models.DateTimeField()

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'payments_subscriptions'