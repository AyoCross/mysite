# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_just_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='just_test',
            field=models.DateTimeField(auto_now=True, verbose_name='用于测试'),
        ),
    ]
