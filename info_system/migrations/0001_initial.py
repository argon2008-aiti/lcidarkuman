# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('marital_status', models.IntegerField(choices=[(0, b'single'), (1, b'married'), (2, b'divorced')])),
                ('house_number', models.CharField(max_length=50)),
                ('street_name', models.CharField(max_length=50)),
                ('suburb', models.CharField(max_length=50)),
                ('location', djgeojson.fields.PointField(null=True)),
            ],
        ),
    ]
