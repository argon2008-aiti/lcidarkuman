# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0029_auto_20170705_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 10, 14), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 10, 14), null=True, blank=True),
        ),
    ]
