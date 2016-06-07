# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-07 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='\u5185\u5bb9')),
                ('click_count', models.IntegerField(default=0, editable=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='\u5206\u7c7b\u540d')),
                ('english_name', models.CharField(max_length=20, unique=True)),
                ('is_on', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u542f')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szu_name', models.CharField(max_length=30)),
                ('nick_name', models.CharField(max_length=30, null=True)),
                ('szu_no', models.CharField(max_length=30, unique=True)),
                ('is_anonymous', models.BooleanField(default=False, verbose_name='\u662f\u5426\u533f\u540d')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='summer_plans.User'),
        ),
        migrations.AddField(
            model_name='plan',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summer_plans.PlanCategory'),
        ),
        migrations.AddField(
            model_name='plan',
            name='like_persons',
            field=models.ManyToManyField(blank=True, related_name='like_persons', to='summer_plans.User'),
        ),
    ]