# Generated by Django 5.0 on 2024-02-16 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_splash_passes_splash'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passes',
            options={'verbose_name': 'Pass', 'verbose_name_plural': 'Passes'},
        ),
    ]
