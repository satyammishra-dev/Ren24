# Generated by Django 5.0 on 2024-02-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_alter_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customticket',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
