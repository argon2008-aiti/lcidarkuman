# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0005_auto_20161107_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ImageField(null=True, upload_to=b'static/profiles/', blank=True),
        ),
    ]
