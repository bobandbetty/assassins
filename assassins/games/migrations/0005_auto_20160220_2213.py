# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 22:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20160220_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='current_target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assassin', to=settings.AUTH_USER_MODEL),
        ),
    ]
