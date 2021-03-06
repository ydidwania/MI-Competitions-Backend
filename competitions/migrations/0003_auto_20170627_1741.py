# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20170627_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='individualevent',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='group',
            name='max_number',
        ),
        migrations.AlterField(
            model_name='individualevent',
            name='participants',
            field=models.ManyToManyField(blank=True, to='participant_api.UserProfile'),
        ),
    ]
