# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-09 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamer', '0002_auto_20160901_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\xa0\xe9\x99\xa4'),
        ),
        migrations.AlterField(
            model_name='register',
            name='college',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xad\xa6\xe9\x99\xa2'),
        ),
        migrations.AlterField(
            model_name='register',
            name='dept1',
            field=models.CharField(choices=[(b'xzb', '\u884c\u653f\u90e8'), (b'sjb', '\u8bbe\u8ba1\u90e8'), (b'jsb', '\u6280\u672f\u90e8'), (b'cbb', '\u91c7\u7f16\u90e8'), (b'yyb', '\u8fd0\u8425\u90e8'), (b'--', '--')], default='cbb', max_length=4, verbose_name=b'\xe7\xac\xac\xe4\xb8\x80\xe5\xbf\x97\xe6\x84\xbf'),
        ),
        migrations.AlterField(
            model_name='register',
            name='dept2',
            field=models.CharField(blank=True, choices=[(b'xzb', '\u884c\u653f\u90e8'), (b'sjb', '\u8bbe\u8ba1\u90e8'), (b'jsb', '\u6280\u672f\u90e8'), (b'cbb', '\u91c7\u7f16\u90e8'), (b'yyb', '\u8fd0\u8425\u90e8'), (b'--', '--')], default='--', max_length=4, null=True, verbose_name=b'\xe7\xac\xac\xe4\xba\x8c\xe5\xbf\x97\xe6\x84\xbf'),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'email'),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[(b'\xe7\x94\xb7', '\u7537'), (b'\xe5\xa5\xb3', '\u5973')], default=b'male', max_length=6, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='register',
            name='grade',
            field=models.CharField(max_length=4, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='register',
            name='self_intro',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name=b'\xe8\x87\xaa\xe6\x88\x91\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='register',
            name='stu_ID',
            field=models.CharField(max_length=10, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7'),
        ),
    ]
