# Generated by Django 2.0.7 on 2019-01-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xbmccontrolroom', '0006_auto_20190101_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='thumbnail',
            field=models.IntegerField(choices=[(0, '일반'), (1, '썸네일용')], default=0, verbose_name='썸네일용'),
        ),
    ]
