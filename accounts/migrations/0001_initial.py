# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.CharField(max_length=50)),
                ('user_type', models.CharField(choices=[('FI', 'Finance'), ('EM', 'Equipment Manager'), ('MM', 'Maintenance Manager'), ('CU', 'Customer')], max_length=2)),
            ],
        ),
    ]
