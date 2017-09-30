# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeforces',
            name='maximum_rating',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='codeforces',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='codeforces_handle',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
