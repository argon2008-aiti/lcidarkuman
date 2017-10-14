# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0010_auto_20170126_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussel',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Inactive'), (1, b'Active')]),
        ),
    ]
