# Generated by Django 4.0.2 on 2022-02-10 21:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^01[0125][0-9]{8}$', 'Egyptian phone number is required')], verbose_name='phone'),
        ),
    ]
