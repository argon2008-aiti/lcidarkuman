# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0011_auto_20170203_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='level_of_education',
            field=models.IntegerField(default=0, choices=[(0, b'None'), (1, b'Primary'), (2, b'Junior High School'), (3, b'Senior High School'), (4, b'First Degree'), (5, b'Second Degree'), (6, b'Doctorate Degree')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 2, 6)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 2, 6)),
        ),
    ]
