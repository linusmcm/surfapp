# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='region',
            field=models.TextField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]