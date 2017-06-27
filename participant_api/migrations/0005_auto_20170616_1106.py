# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participant_api', '0004_auto_20170616_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mi_number',
            field=models.CharField(default='default', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='postal_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='present_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participant_api.City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='present_college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participant_api.College'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_of_study',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth')], max_length=7),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]