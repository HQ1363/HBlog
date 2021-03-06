# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-14 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191208_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.SmallIntegerField(default=2, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='visitors',
            field=models.BigIntegerField(default=0, verbose_name='\u8bbf\u95ee\u91cf'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.Blog', verbose_name='\u535a\u5ba2'),
        ),
    ]
