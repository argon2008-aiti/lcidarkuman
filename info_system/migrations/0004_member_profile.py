# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0003_auto_20161103_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
