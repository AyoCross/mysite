# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20161120_1338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Choicess',
        ),
    ]
