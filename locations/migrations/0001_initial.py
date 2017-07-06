# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('best_wind_direct', models.CharField(max_length=30)),
                ('break_type', models.TextField(max_length=100)),
                ('local_attitude', models.TextField(max_length=100)),
                ('best_wind', models.TextField(max_length=100)),
                ('best_tide', models.TextField(max_length=100)),
                ('wave_type', models.TextField(max_length=100)),
                ('who_are_locals_ID', models.TextField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country')),
            ],
        ),
    ]
