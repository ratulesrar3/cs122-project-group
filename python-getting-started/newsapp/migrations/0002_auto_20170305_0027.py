# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-05 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField()),
                ('homepage', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.TextField()),
                ('author', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
                ('nltk_score', models.IntegerField(default=0)),
                ('article_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.Forum')),
            ],
        ),
        migrations.CreateModel(
            name='ProPublica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
                ('nltk_score', models.IntegerField(default=0)),
                ('article_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.Forum')),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
