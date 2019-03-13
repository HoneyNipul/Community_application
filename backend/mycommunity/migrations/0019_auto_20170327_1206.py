# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0018_auto_20170327_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitelist',
            name='inviterId',
        ),
        migrations.AddField(
            model_name='invitelist',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mycommunity.events'),
            preserve_default=False,
        ),
    ]