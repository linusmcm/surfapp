# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20161220_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='customer',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='paid',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='receipt_number',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='status',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='time_created',
            field=models.DateField(auto_now=True),
        ),
    ]
