# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billjobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is available ?'),
        ),
    ]
