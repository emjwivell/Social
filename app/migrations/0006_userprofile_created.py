# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 05:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160307_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 8, 5, 9, 14, 486205, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
