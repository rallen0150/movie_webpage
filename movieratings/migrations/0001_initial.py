# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=30)),
                ('video_release_date', models.CharField(max_length=30)),
                ('imdb_url', models.CharField(max_length=150)),
                ('unknown', models.CharField(max_length=50)),
                ('action_genre', models.BooleanField()),
                ('adventure', models.BooleanField()),
                ('animation', models.BooleanField()),
                ('children', models.BooleanField()),
                ('comedy', models.BooleanField()),
                ('crime', models.BooleanField()),
                ('documentary', models.BooleanField()),
                ('drama', models.BooleanField()),
                ('fantasy', models.BooleanField()),
                ('film_noir', models.BooleanField()),
                ('horror', models.BooleanField()),
                ('musical', models.BooleanField()),
                ('mystery', models.BooleanField()),
                ('romance', models.BooleanField()),
                ('sci_fi', models.BooleanField()),
                ('thriller', models.BooleanField()),
                ('war', models.BooleanField()),
                ('western', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('time_stamp', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Rater')),
            ],
        ),
    ]