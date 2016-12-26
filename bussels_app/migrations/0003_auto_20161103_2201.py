# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0002_auto_20161103_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bussel',
            old_name='passcode',
            new_name='password',
        ),
    ]
