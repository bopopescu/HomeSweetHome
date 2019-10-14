# Generated by Django 2.1.5 on 2019-05-21 18:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('xbmccontrolroom', '0013_mediafile_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediafile',
            name='tags',
        ),
        migrations.AddField(
            model_name='mediafile',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
