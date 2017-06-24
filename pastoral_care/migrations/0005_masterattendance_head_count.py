# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0004_masterattendance_attendance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterattendance',
            name='head_count',
            field=models.IntegerField(default=0),
        ),
    ]
