# Generated by Django 4.2.9 on 2024-02-07 15:30

import apps.users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='color',
            new_name='color1',
        ),
        migrations.AddField(
            model_name='user',
            name='color2',
            field=models.CharField(default=apps.users.utils.random_hex, max_length=7),
        ),
        migrations.AddField(
            model_name='user',
            name='color3',
            field=models.CharField(default=apps.users.utils.random_hex, max_length=7),
        ),
        migrations.AddField(
            model_name='user',
            name='color4',
            field=models.CharField(default=apps.users.utils.random_hex, max_length=7),
        ),
        migrations.AddField(
            model_name='user',
            name='color5',
            field=models.CharField(default=apps.users.utils.random_hex, max_length=7),
        ),
    ]
