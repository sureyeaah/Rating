# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20170930_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeforces',
            name='maximum_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='codeforces',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
