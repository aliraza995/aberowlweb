# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aberowl', '0007_auto_20171023_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='version',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
