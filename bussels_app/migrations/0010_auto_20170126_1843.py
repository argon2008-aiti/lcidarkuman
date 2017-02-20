# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0009_bussel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busselreport',
            name='date',
            field=models.DateField(),
        ),
    ]
