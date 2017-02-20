# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0008_auto_20170127_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 1, 30)),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 1, 30)),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ImageField(default=b'static/profiles/banner1.png', upload_to=b'static/profiles/', blank=True),
        ),
    ]
