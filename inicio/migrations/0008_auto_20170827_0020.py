# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 05:20
from __future__ import unicode_literals

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20170826_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='peso_neto',
            field=django_mysql.models.EnumField(choices=[('t', 'Si'), ('f', 'No')]),
        ),
    ]