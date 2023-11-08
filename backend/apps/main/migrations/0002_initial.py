# Generated by Django 4.2.6 on 2023-11-05 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertheme",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="link",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="core.telegramstorage"
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="chat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="main.chat",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="chat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="main.chat",
            ),
        ),
    ]