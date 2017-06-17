# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterattendance',
            name='in_session',
            field=models.BooleanField(default=False),
        ),
    ]
