# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_locations_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='locations',
            new_name='Location',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Locations'},
        ),
    ]
