# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_auto_20170726_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('AQ', 'Awaiting Quotation'), ('AR', 'Awaiting Confirmation'), ('CO', 'Confirmed'), ('RE', 'Rejected')], max_length=2),
        ),
    ]
