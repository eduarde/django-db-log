# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-29 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_db_log', '0002_auto_20180829_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debuglog',
            options={'verbose_name': 'System Log Entry', 'verbose_name_plural': 'System Log Entries'},
        ),
        migrations.AlterModelOptions(
            name='errorlog',
            options={'verbose_name': 'System Log Entry', 'verbose_name_plural': 'System Log Entries'},
        ),
        migrations.AlterModelOptions(
            name='generallog',
            options={'verbose_name': 'System Log Entry', 'verbose_name_plural': 'System Log Entries'},
        ),
        migrations.AlterModelOptions(
            name='infolog',
            options={'verbose_name': 'System Log Entry', 'verbose_name_plural': 'System Log Entries'},
        ),
    ]
