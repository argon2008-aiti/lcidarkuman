# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0012_auto_20180706_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussellMemberAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bussell_attendance', models.BooleanField(default=False)),
                ('church_attendance', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='bussellmember',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busselreport',
            name='notes',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='bussel',
            name='group_pic',
            field=models.URLField(max_length=400, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bussellmemberattendance',
            name='bussell_member',
            field=models.ForeignKey(to='bussels_app.BussellMember'),
        ),
        migrations.AddField(
            model_name='bussellmemberattendance',
            name='bussell_report',
            field=models.ForeignKey(to='bussels_app.BusselReport'),
        ),
    ]
