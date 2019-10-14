# Generated by Django 2.0.7 on 2018-08-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0020_auto_20180817_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='spending',
            options={'verbose_name_plural': 'Spending'},
        ),
        migrations.AlterModelOptions(
            name='wealth',
            options={'verbose_name_plural': 'Wealth'},
        ),
        migrations.AddField(
            model_name='deal',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='longuitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]