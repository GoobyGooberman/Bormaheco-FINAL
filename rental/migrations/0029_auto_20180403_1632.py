# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-03 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0028_incident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='quotation_equipment',
        ),
        migrations.DeleteModel(
            name='Incident',
        ),
    ]
