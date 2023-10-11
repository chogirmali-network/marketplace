# Generated by Django 4.2.3 on 2023-09-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_s3attachment_created_at_s3attachment_deleted_at_and_more"),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
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
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("group", "Group"), ("private", "Private")],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "db_table": "chats",
            },
        ),
        migrations.AlterModelOptions(
            name="usertheme",
            options={"ordering": ("id",)},
        ),
        migrations.RemoveField(
            model_name="message",
            name="chat_id",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="chat_id",
        ),
        migrations.AlterField(
            model_name="theme",
            name="link",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="core.telegramstorage"
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="chat",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="main.chat",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="notification",
            name="chat",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="main.chat",
            ),
            preserve_default=False,
        ),
    ]