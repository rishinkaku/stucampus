# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-11 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer_plans', '0005_auto_20160611_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_anon',
        ),
        migrations.AddField(
            model_name='plan',
            name='alias',
            field=models.CharField(blank=True, default='\u533f\u540d', max_length=10, null=True, verbose_name='\u533f\u540d\u6635\u79f0'),
        ),
        migrations.AddField(
            model_name='plan',
            name='is_anon',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u533f\u540d'),
        ),
    ]
