# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name_plural': 'Payments'},
        ),
        migrations.RemoveField(
            model_name='payments',
            name='charge_outcome',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='charge_paid',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='user',
        ),
    ]