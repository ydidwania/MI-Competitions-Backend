# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informals', '0003_auto_20170626_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='informalsgenre',
            name='genre',
            field=models.CharField(default='as', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infromalsevent',
            name='name',
            field=models.CharField(default='as', max_length=100),
            preserve_default=False,
        ),
    ]