# Generated by Django 2.0.7 on 2018-07-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0007_auto_20180725_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='images/product/'),
        ),
    ]