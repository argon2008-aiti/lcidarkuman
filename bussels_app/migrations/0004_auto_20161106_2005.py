# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0003_auto_20161103_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busselreport',
            old_name='bussel_attend',
            new_name='bussel_attendance',
        ),
        migrations.RenameField(
            model_name='busselreport',
            old_name='church_attend',
            new_name='church_attendance',
        ),
        migrations.RenameField(
            model_name='busselreport',
            old_name='souls_won',
            new_name='num_first_timers',
        ),
        migrations.RenameField(
            model_name='busselreport',
            old_name='offertory',
            new_name='offertory_given',
        ),
        migrations.AddField(
            model_name='busselreport',
            name='bussel',
            field=models.ForeignKey(default=0, to='bussels_app.Bussel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busselreport',
            name='num_souls_won',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
