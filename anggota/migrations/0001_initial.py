# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-30 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrp', models.CharField(max_length=9)),
                ('nama', models.CharField(max_length=45)),
                ('alamat', models.TextField(blank=True)),
                ('no_telp', models.CharField(max_length=12)),
                ('foto', models.ImageField(blank=True, upload_to='upload')),
            ],
        ),
    ]
