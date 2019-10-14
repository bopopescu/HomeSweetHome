# Generated by Django 2.1.4 on 2018-12-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xbmccontrolroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onair',
            options={'verbose_name': 'OnAir', 'verbose_name_plural': 'OnAir'},
        ),
        migrations.AlterModelOptions(
            name='xbmcmediahost',
            options={'verbose_name': 'Xbmc Media Host', 'verbose_name_plural': 'Xbmc Media Hosts'},
        ),
        migrations.AlterField(
            model_name='xbmcmediahost',
            name='macaddress',
            field=models.CharField(max_length=17, unique=True, verbose_name='MAC주소'),
        ),
    ]
