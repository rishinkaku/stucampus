# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-11-15 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='content',
            field=models.CharField(max_length=50000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
