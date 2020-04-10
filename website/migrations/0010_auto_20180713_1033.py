# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-13 15:33
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170903_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(blank=True, max_length=10000, null=True)),
                ('artist_name', models.CharField(blank=True, max_length=10000, null=True)),
                ('date_reviewed', models.DateField(blank=True, null=True)),
                ('review_text', models.TextField(blank=True, max_length=1000000, null=True)),
                ('album_image', models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/usr/share/nginx/html/media/'))),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_image',
            field=models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/usr/share/nginx/html/media/')),
        ),
    ]