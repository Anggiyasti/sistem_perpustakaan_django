# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_buku', models.CharField(max_length=10)),
                ('judul_buku', models.CharField(max_length=100)),
                ('pengarang', models.CharField(max_length=100)),
            ],
        ),
    ]
