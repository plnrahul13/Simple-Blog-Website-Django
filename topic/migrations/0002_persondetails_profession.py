# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondetails',
            name='profession',
            field=models.CharField(default='Not Working', max_length=500),
            preserve_default=False,
        ),
    ]
