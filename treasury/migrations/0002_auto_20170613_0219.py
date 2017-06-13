# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('treasury', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tithe',
            name='date',
            field=models.DateField(default=django.utils.datetime_safe.datetime.today, auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tithe',
            name='month',
            field=models.IntegerField(choices=[(0, b'January'), (1, b'February'), (2, b'March'), (3, b'April'), (4, b'May'), (5, b'June'), (6, b'July'), (7, b'August'), (8, b'September'), (9, b'October'), (10, b'November'), (11, b'December')]),
        ),
    ]
