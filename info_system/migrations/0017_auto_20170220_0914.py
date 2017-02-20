# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0016_auto_20170220_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='hometown',
            field=models.CharField(default=b'Madina, Greater Accra, Ghana', max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='tribal_origin',
            field=models.CharField(default=b'Asante, Asante Region, Ghana', max_length=200),
        ),
    ]
