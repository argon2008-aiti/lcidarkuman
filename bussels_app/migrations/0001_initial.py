# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bussel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('passcode', models.CharField(max_length=50)),
                ('bussel_location', djgeojson.fields.PointField(null=True)),
                ('leader', models.ForeignKey(to='info_system.Member')),
            ],
        ),
        migrations.CreateModel(
            name='BusselReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time_started', models.TimeField()),
                ('time_ended', models.TimeField()),
                ('bussel_attend', models.IntegerField()),
                ('church_attend', models.IntegerField()),
                ('souls_won', models.IntegerField()),
                ('offertory', models.FloatField()),
            ],
        ),
    ]
