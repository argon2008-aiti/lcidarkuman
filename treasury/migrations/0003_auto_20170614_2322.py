# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasury', '0002_auto_20170613_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='week_number',
            field=models.IntegerField(default=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tithe',
            name='week_number',
            field=models.IntegerField(default=24),
            preserve_default=False,
        ),
    ]
