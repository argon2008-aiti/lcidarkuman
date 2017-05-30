# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0018_auto_20170530_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to='info_system.Member')),
            ],
        ),
    ]
