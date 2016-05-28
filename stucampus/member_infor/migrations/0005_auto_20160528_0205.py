# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-27 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_infor', '0004_remove_member_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='\u901a\u8fc7\u8ba4\u8bc1'),
        ),
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AddField(
            model_name='member',
            name='e_mail',
            field=models.EmailField(blank=True, max_length=30, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AddField(
            model_name='member',
            name='nick_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u522b\u540d'),
        ),
    ]