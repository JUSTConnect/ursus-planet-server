# Generated by Django 5.0.1 on 2024-01-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccountTelegramCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('uuid', models.UUIDField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
