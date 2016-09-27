# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 16:03
from __future__ import unicode_literals

import apps.login_reg_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[apps.login_reg_app.models.validateName])),
                ('last_name', models.CharField(max_length=255, validators=[apps.login_reg_app.models.validateName])),
                ('email', models.EmailField(max_length=254)),
                ('feet', models.IntegerField()),
                ('inches', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
