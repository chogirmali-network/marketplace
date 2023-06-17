# Generated by Django 3.2.16 on 2023-06-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=155, verbose_name='Kimdan..?')),
                ('Content', models.TextField()),
                ('why', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
                ('is_view', models.BooleanField()),
            ],
        ),
    ]