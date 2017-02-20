# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0010_auto_20170203_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nationality',
            field=models.IntegerField(choices=[(0, b'Ghanaian'), (1, b'Nigerian'), (2, b'Togolese'), (3, b'Beninois')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='nationality_at_birth',
            field=models.IntegerField(choices=[(0, b'Ghanaian'), (1, b'Nigerian'), (2, b'Togolese'), (3, b'Beninois')]),
        ),
    ]
