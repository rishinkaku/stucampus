# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-12-06 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0002_gift_isget'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftsystem_user',
            name='gender',
            field=models.CharField(choices=[(b'male', '\u7537'), (b'female', '\u5973')], default=b'male', max_length=6, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='giftsystem_user',
            name='area',
            field=models.CharField(choices=[(b'C', '\u5357\u533a'), (b'A', '\u897f\u5357'), (b'B', '\u658b\u533a')], default=b'C', max_length=1, null=True, verbose_name=b'\xe5\xb1\x85\xe4\xbd\x8f\xe5\x8c\xba\xe5\x9f\x9f'),
        ),
    ]
