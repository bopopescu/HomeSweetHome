# Generated by Django 2.1.4 on 2018-12-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xbmccontrolroom', '0003_auto_20181220_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='파일명')),
                ('path', models.CharField(max_length=255, unique=True, verbose_name='경로')),
                ('md5', models.CharField(max_length=255, verbose_name='MD5')),
                ('updDate', models.DateTimeField(auto_now_add=True, verbose_name='기록 일시')),
            ],
        ),
    ]