# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20191221_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='career',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
