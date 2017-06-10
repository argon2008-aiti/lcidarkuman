# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0019_auto_20170610_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2048)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('authorized_by', models.ForeignKey(to='info_system.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master_attendance', models.ForeignKey(to='pastoral_care.MasterAttendance')),
                ('member', models.ForeignKey(to='info_system.Member')),
            ],
        ),
    ]
