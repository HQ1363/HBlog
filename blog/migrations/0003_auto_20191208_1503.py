# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-08 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191201_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='\u5206\u7c7b'),
        ),
    ]