# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-04 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0021_invitelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_registery',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
        migrations.AlterField(
            model_name='eventnotification',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
        migrations.AlterField(
            model_name='invitelist',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Events'),
        ),
    ]