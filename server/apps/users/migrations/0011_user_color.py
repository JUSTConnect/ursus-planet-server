# Generated by Django 4.2.9 on 2024-02-07 15:29

import apps.users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_points_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(default=apps.users.utils.random_hex, max_length=7),
        ),
    ]
