# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'ordering': ('title',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='app.Category')),
            ],
            options={
                'verbose_name': 'menu',
                'ordering': ('title',),
                'verbose_name_plural': 'menus',
            },
        ),
        migrations.CreateModel(
            name='NewsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sub_title', models.CharField(blank=True, max_length=250)),
                ('detail', models.TextField()),
                ('category', models.CharField(choices=[('Event', 'Event'), ('News', 'News')], max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'newsevent',
                'ordering': ('-created',),
                'verbose_name_plural': 'newsevents',
            },
        ),
    ]
