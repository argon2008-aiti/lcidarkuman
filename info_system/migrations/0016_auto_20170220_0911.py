# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0015_auto_20170207_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='hometown',
            field=models.CharField(default=b'Accra', max_length=200),
        ),
        migrations.AddField(
            model_name='member',
            name='tribal_origin',
            field=models.CharField(default=b'Asante', max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 2, 20)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 2, 20)),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.IntegerField(default=0, choices=[(0, b'Single'), (1, b'Married'), (2, b'Separated'), (3, b'Divorced'), (4, b'Widowed')]),
        ),
        migrations.AddField(
            model_name='attendance',
            name='member',
            field=models.ForeignKey(to='info_system.Member'),
        ),
    ]
