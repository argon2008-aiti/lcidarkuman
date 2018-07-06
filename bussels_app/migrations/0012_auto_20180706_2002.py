# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussels_app', '0011_bussel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussellMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('date_of_birth', models.DateField()),
                ('date_joined', models.DateField()),
                ('gender', models.IntegerField(default=0, choices=[(0, b'Male'), (1, b'Female')])),
                ('church_member', models.BooleanField(default=False)),
                ('profile_pic', models.URLField(max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bussel',
            name='group_pic',
            field=models.URLField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='bussellmember',
            name='bussell',
            field=models.ForeignKey(to='bussels_app.Bussel'),
        ),
    ]
