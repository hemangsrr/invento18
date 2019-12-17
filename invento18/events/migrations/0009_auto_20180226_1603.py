# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_townscript_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='_type',
            field=models.CharField(choices=[('wor', 'Workshops'), ('com', 'Competitions'), ('sho', 'Shows'), ('oth', 'Other')], default='wor', max_length=3, verbose_name='Title'),
        ),
    ]
