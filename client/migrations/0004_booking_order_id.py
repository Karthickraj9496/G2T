# Generated by Django 5.2.1 on 2025-05-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
