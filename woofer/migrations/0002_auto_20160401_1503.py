# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-01 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woofer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wooferuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='wooferuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='wooferuser',
            name='last_name',
        ),
    ]