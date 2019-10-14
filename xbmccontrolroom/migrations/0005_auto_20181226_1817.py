# Generated by Django 2.1.4 on 2018-12-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xbmccontrolroom', '0004_mediafile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='size',
            field=models.IntegerField(default=0, verbose_name='파일크기'),
        ),
        migrations.AddField(
            model_name='onair',
            name='action',
            field=models.CharField(default='', max_length=64, verbose_name='동작 명령'),
        ),
        migrations.AddField(
            model_name='onair',
            name='action_param',
            field=models.CharField(default='', max_length=255, verbose_name='동작 명령 매개변수'),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='path',
            field=models.TextField(verbose_name='경로'),
        ),
    ]