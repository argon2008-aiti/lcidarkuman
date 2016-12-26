# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussel',
            name='house_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bussel',
            name='street_name',
            field=models.CharField(default='k', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bussel',
            name='suburb',
            field=models.CharField(default='u', max_length=50),
            preserve_default=False,
        ),
    ]
