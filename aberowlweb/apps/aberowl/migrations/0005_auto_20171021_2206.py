# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aberowl', '0004_submission_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='version',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='documentation',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='has_ontology_language',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='submission',
            name='home_page',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='publication',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]
