# Generated by Django 4.2.7 on 2024-01-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_userid_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
