# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-01 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woofer', '0002_auto_20160401_1503'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dogs',
            new_name='Dog',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
