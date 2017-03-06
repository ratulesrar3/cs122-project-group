# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.FloatField(default=0)),
                ('country', models.TextField()),
                ('date', models.ManyToManyField(to='newsapp.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close', models.FloatField(default=0)),
                ('ticker', models.TextField()),
                ('date', models.ManyToManyField(to='newsapp.Article')),
            ],
        ),
    ]
