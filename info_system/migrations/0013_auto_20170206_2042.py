# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0012_auto_20170206_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='lingual_competency',
            field=models.CommaSeparatedIntegerField(default=0, max_length=100, choices=[(0, b'English'), (1, b'French'), (2, b'Akan'), (3, b'Ga'), (4, b'Ewe'), (5, b'Hausa')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(default=b'Unemployed', max_length=100),
        ),
    ]
