# Generated by Django 2.0.7 on 2018-08-17 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0019_auto_20180816_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='type_flag',
            field=models.IntegerField(choices=[(0, '현금성'), (1, '현물'), (2, '채권'), (3, '유가증권'), (4, '외환')], default=0, verbose_name='유형 구분'),
        ),
        migrations.AddField(
            model_name='deal',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountbook.Person', verbose_name='구성원'),
        ),
    ]
