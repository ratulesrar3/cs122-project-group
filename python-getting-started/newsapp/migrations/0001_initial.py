# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date_published')),
                ('nltk_score', models.FloatField(default=0)),
                ('source', models.TextField()),
            ],
        ),
    ]
