# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-24 04:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='created_by',
        ),
    ]
