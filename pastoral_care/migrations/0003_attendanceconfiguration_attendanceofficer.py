# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_care', '0002_masterattendance_in_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance_in_session', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceOfficer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shepherd_pk', models.IntegerField()),
                ('assigned_members', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]
