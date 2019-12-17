# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-24 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180211_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('wor', 'Workshops'), ('com', 'Competitions')], default='wor', max_length=3),
        ),
        migrations.AlterField(
            model_name='imageurl',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_urls', to='events.Event'),
        ),
    ]
