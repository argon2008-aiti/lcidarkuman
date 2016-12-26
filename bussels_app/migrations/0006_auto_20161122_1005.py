# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0005_auto_20161113_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busselreport',
            options={'get_latest_by': 'date'},
        ),
        migrations.AddField(
            model_name='busselreport',
            name='time',
            field=models.TimeField(default=datetime.time(10, 5, 32, 416891), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bussel',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='busselreport',
            name='church_attendance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='busselreport',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
