# Generated by Django 2.1.5 on 2019-01-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0032_auto_20190112_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='receipt',
            field=models.ImageField(blank=True, help_text='영수증', max_length=1000, upload_to='images/deal/', verbose_name='첨부 파일'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='attached_file',
            field=models.FileField(blank=True, help_text='내역서, 설명서 등', max_length=1000, upload_to='images/deal/attached/', verbose_name='첨부 파일'),
        ),
    ]
