# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_system', '0018_auto_20170530_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shepherd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='member',
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 6, 10), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 6, 10), null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.AddField(
            model_name='shepherd',
            name='member',
            field=models.ForeignKey(to='info_system.Member'),
        ),
        migrations.AddField(
            model_name='shepherd',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
