# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='measuring_unit',
            new_name='price',
        ),
    ]