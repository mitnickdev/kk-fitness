# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blueSquirrelsFitnessApp', '0005_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
