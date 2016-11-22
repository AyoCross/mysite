# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20161121_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(blank=True, choices=[('D', '等待处理'), ('Y', '已经处理'), ('Z', '正在处理')], max_length=1),
        ),
    ]