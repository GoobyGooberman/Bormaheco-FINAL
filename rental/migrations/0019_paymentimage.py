# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-13 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0018_auto_20171213_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentImage', models.ImageField(default='../media/paymentimages/defaultpayment.png', upload_to='paymentimages')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Quotation')),
            ],
        ),
    ]
