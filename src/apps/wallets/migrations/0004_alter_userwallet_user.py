# Generated by Django 5.0.1 on 2024-01-15 02:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0003_projectwallet_chain_userwallet_chain'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wallets', to=settings.AUTH_USER_MODEL),
        ),
    ]
