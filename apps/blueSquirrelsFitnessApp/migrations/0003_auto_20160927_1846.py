# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blueSquirrelsFitnessApp', '0002_auto_20160927_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_id',
            new_name='food',
        ),
    ]