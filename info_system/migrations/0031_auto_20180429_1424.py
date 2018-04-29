# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0030_auto_20171014_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2018, 4, 29), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2018, 4, 29), null=True, blank=True),
        ),
    ]
