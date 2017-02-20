# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0013_auto_20170206_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 2, 7)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 2, 7)),
        ),
        migrations.RemoveField(
            model_name='member',
            name='lingual_competency',
        ),
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ImageField(default=b'static/profiles/default.png', upload_to=b'static/profiles/', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='lingual_competency',
            field=models.ManyToManyField(to='info_system.Language', null=True, blank=True),
        ),
    ]
