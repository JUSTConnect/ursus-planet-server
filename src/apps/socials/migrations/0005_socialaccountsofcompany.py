# Generated by Django 4.2.9 on 2024-03-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0004_alter_socialaccounttelegramcode_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccountsOfCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord', models.URLField()),
                ('x', models.URLField()),
                ('telegram', models.URLField()),
                ('github', models.URLField()),
                ('instagram', models.URLField()),
                ('reddit', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
