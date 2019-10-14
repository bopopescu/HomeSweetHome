# Generated by Django 2.0.7 on 2018-08-21 23:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0021_auto_20180820_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AlterField(
            model_name='deal',
            name='longuitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
    ]
