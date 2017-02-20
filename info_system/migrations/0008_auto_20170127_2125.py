# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0007_auto_20170126_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nationality_at_birth',
            field=models.IntegerField(default=0, choices=[(0, b'Ghanaian'), (1, b'Nigerian'), (2, b'Togolese'), (3, b'Beninois')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 1, 27)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 1, 27)),
        ),
    ]
