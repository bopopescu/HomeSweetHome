# Generated by Django 2.1.5 on 2019-05-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0034_auto_20190208_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='memo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='메모'),
        ),
    ]