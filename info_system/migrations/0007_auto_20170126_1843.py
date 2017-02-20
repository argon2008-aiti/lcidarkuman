# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_system', '0006_auto_20161113_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='baptized_by_immersion',
            field=models.IntegerField(default=1, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateField(default=datetime.date(2017, 1, 26)),
        ),
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2017, 1, 26)),
        ),
        migrations.AddField(
            model_name='member',
            name='description_of_house',
            field=models.CharField(default='description', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='email_address',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='holy_ghost_baptism',
            field=models.IntegerField(default=0, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='member',
            name='leadership_role',
            field=models.IntegerField(default=0, choices=[(0, b'None'), (1, b'Pastor'), (2, b'Lady Pastor'), (3, b'Bussell Leader'), (4, b'Ministry Leader')]),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_status',
            field=models.IntegerField(default=1, choices=[(0, b'Inactive'), (1, b'Active')]),
        ),
        migrations.AddField(
            model_name='member',
            name='nationality',
            field=models.IntegerField(default=0, choices=[(0, b'Ghanaian'), (1, b'Nigerian'), (2, b'Togolese'), (3, b'Beninois')]),
        ),
        migrations.AddField(
            model_name='member',
            name='place_of_birth',
            field=models.CharField(default=b'Accra', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='ministries',
            field=models.ManyToManyField(to='info_system.Ministry'),
        ),
    ]
