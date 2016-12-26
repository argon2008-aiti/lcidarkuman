# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0002_auto_20161103_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='location',
            new_name='member_location',
        ),
    ]
