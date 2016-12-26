# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0004_auto_20161106_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussel',
            name='meeting_day',
            field=models.IntegerField(default=6, choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bussel',
            name='meeting_time',
            field=models.TimeField(default=datetime.time(18, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bussel',
            name='zone',
            field=models.CharField(default='A1', max_length=5),
            preserve_default=False,
        ),
    ]
