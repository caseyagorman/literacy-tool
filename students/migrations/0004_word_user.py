# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-24 05:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0003_auto_20180723_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]