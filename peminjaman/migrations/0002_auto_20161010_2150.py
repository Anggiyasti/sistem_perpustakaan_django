# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-10 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjaman',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
