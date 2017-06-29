# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0006_attendanceofficer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterattendance',
            name='first_timers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendanceofficer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
