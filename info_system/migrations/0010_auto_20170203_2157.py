# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0009_auto_20170130_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 2, 3)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 2, 3)),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.IntegerField(default=0, choices=[(0, b'Single'), (1, b'Married'), (2, b'Divorced')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='ministries',
            field=models.ManyToManyField(to='info_system.Ministry', null=True, blank=True),
        ),
    ]
