# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 18:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20170822_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymember',
            name='role',
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(4),
                    django.core.validators.MinValueValidator(1)]),
        ),
    ]
