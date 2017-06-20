# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0003_attendanceconfiguration_attendanceofficer'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterattendance',
            name='attendance_type',
            field=models.IntegerField(default=0, choices=[(0, b'Sunday Morning Service'), (1, b'Wednesday Evening Service'), (2, b'Shepherds Meeting'), (3, b'Other')]),
        ),
    ]
