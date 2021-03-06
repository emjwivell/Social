# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160307_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suggestion',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='alcohol',
            old_name='name',
            new_name='alcohol_type',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='following',
        ),
        migrations.AddField(
            model_name='follower',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(to='app.Follower'),
        ),
    ]
