# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160929_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题描述'),
        ),
    ]
