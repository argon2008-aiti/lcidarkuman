# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0006_auto_20161122_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busselreport',
            name='date',
            field=models.DateField(),
        ),
    ]
