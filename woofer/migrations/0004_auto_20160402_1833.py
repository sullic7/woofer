# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-02 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('woofer', '0003_auto_20160401_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wooferuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]