# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-19 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_auto_20161005_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='youtube_url',
            field=models.URLField(blank=True, default=b'', null=True),
        ),
    ]
