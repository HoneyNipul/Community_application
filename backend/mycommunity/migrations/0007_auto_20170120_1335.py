# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycommunity', '0006_auto_20170120_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('married', 'married'), ('unmarried', 'unmarried'), ('divorce', 'divorce'), ('widow', 'widow'), ('widower', 'widower')], max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number1',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number2',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='office_number',
            field=models.CharField(max_length=16),
        ),
    ]
