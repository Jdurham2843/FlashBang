# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cardCount', models.IntegerField(default=0)),
            ],
        ),
    ]
