# Generated by Django 5.0 on 2023-12-28 04:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='userid',
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
