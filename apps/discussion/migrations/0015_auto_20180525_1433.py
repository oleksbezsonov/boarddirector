# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0014_listrequestschannels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='listrequestschannels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]