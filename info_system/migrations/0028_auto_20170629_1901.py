# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0027_auto_20170628_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 6, 29), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 6, 29), null=True, blank=True),
        ),
    ]
