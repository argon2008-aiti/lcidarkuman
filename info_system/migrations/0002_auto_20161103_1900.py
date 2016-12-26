# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.IntegerField(default=0, choices=[(0, b'Male'), (1, b'Female')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.IntegerField(default=0, choices=[(0, b'single'), (1, b'married'), (2, b'divorced')]),
        ),
    ]
