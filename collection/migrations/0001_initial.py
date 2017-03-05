# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 19:45
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
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_price', models.IntegerField(default=0)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Category')),
            ],
        ),
    ]
