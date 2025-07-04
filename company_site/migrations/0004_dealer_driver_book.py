# Generated by Django 5.2 on 2025-05-18 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_site', '0003_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mob', models.CharField(max_length=20)),
                ('nature', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('from_state', models.CharField(max_length=100)),
                ('from_city', models.CharField(max_length=100)),
                ('to_state', models.CharField(max_length=100)),
                ('to_city', models.CharField(max_length=100)),
                ('rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mob', models.CharField(max_length=20)),
                ('truck_no', models.CharField(max_length=20)),
                ('truck_capacity', models.IntegerField()),
                ('transporter_name', models.CharField(max_length=100)),
                ('driving_experience', models.IntegerField()),
                ('from_state1', models.CharField(max_length=100)),
                ('from_city1', models.CharField(max_length=100)),
                ('to_state1', models.CharField(max_length=100)),
                ('to_city1', models.CharField(max_length=100)),
                ('from_state2', models.CharField(max_length=100)),
                ('from_city2', models.CharField(max_length=100)),
                ('to_state2', models.CharField(max_length=100)),
                ('to_city2', models.CharField(max_length=100)),
                ('from_state3', models.CharField(max_length=100)),
                ('from_city3', models.CharField(max_length=100)),
                ('to_state3', models.CharField(max_length=100)),
                ('to_city3', models.CharField(max_length=100)),
                ('rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_site.dealer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_site.driver')),
            ],
        ),
    ]
