# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20171014_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status_pco',
            old_name='IDProductoCampo',
            new_name='IDProductoCorrida',
        ),
    ]
