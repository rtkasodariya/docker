# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20160411_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_path',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_tags',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
