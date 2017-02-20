# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0014_auto_20170207_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='lingual_competency',
            field=models.ManyToManyField(to='info_system.Language'),
        ),
    ]
