# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0022_auto_20171214_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentimage',
            name='created_by',
        ),
        migrations.AddField(
            model_name='paymentimage',
            name='quotation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rental.Quotation'),
            preserve_default=False,
        ),
    ]