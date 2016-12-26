# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0008_auto_20161124_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussel',
            name='date_created',
            field=models.DateField(default=datetime.date(2016, 12, 19), auto_now_add=True),
            preserve_default=False,
        ),
    ]
