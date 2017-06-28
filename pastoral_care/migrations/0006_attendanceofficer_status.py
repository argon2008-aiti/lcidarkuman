# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0005_masterattendance_head_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendanceofficer',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
