# Generated by Django 5.2.1 on 2025-05-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status_by_client',
            field=models.BooleanField(default=True),
        ),
    ]
