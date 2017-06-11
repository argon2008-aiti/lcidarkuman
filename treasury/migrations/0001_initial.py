# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0020_auto_20170611_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=64)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tithe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('member', models.ForeignKey(to='info_system.Member')),
            ],
        ),
    ]
