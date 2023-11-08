# Generated by Django 4.2.6 on 2023-11-07 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StripeSubscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default=False,
                        max_length=20,
                    ),
                ),
                ("subscription_id", models.CharField(max_length=50)),
                ("customer_id", models.CharField(max_length=50)),
                (
                    "billing_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MyStripeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "stripe_subscription",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="payments.stripesubscription",
                    ),
                ),
            ],
        ),
    ]