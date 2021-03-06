# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(default='', max_length=200)),
                ('address_line2', models.CharField(default='', max_length=200)),
                ('landmark', models.CharField(default='', max_length=100)),
                ('area', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('country', models.BooleanField()),
                ('postal_code', models.IntegerField(max_length=16)),
                ('phone_number1', models.CharField(max_length=10)),
                ('phone_number2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='event_registery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'Event_Registery',
            },
        ),
        migrations.CreateModel(
            name='eventnotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(max_length=200)),
                ('notification_description', models.TextField()),
                ('notification_start', models.DateField()),
                ('notification_end', models.DateField()),
            ],
            options={
                'db_table': 'Event_notification',
            },
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_description', models.TextField(max_length=3000)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('event_type', models.BooleanField()),
                ('is_open_event', models.BooleanField()),
                ('Send_last_notification_before', models.DateField()),
                ('event_photo', models.CharField(max_length=3000)),
            ],
            options={
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Group',
            },
        ),
        migrations.CreateModel(
            name='group_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.group')),
            ],
            options={
                'db_table': 'Group_Member',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=100)),
                ('marital_status', models.BooleanField()),
                ('mobile_number1', models.CharField(max_length=10)),
                ('mobile_number2', models.CharField(max_length=10)),
                ('office_number', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=1000)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Address')),
            ],
            options={
                'db_table': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to='mycommunity.Member')),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_person_user', to='mycommunity.Member')),
            ],
            options={
                'db_table': 'Relation',
            },
        ),
        migrations.AddField(
            model_name='group_member',
            name='mem_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Member'),
        ),
        migrations.AddField(
            model_name='group',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Member'),
        ),
        migrations.AddField(
            model_name='events',
            name='inviters_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Member'),
        ),
        migrations.AddField(
            model_name='eventnotification',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.events'),
        ),
        migrations.AddField(
            model_name='event_registery',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.events'),
        ),
        migrations.AddField(
            model_name='event_registery',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycommunity.Member'),
        ),
    ]
