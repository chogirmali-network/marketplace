# Generated by Django 4.2 on 2023-08-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]