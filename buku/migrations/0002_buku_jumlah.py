# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-16 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jumlah',
            field=models.IntegerField(null=True),
        ),
    ]
