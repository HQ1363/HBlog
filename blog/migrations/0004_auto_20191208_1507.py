# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-08 07:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191208_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categories',
        ),
    ]
