# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('info_system', '0017_auto_20170220_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 5, 30), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 5, 30), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='description_of_house',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='hometown',
            field=models.CharField(default=b'Madina, Greater Accra, Ghana', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='house_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='middle_name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.CharField(default=b'Unemployed', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='place_of_birth',
            field=models.CharField(default=b'Accra', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='street_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='suburb',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='tribal_origin',
            field=models.CharField(default=b'Asante, Asante Region, Ghana', max_length=200, null=True, blank=True),
        ),
    ]
