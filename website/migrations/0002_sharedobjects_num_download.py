# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-02 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedobjects',
            name='num_download',
            field=models.IntegerField(default=0),
        ),
    ]
