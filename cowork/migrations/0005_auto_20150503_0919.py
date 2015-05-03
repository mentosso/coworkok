# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0004_auto_20150501_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='company_logos', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='location',
            name='postal_code',
            field=models.CharField(max_length=6, verbose_name='Postal code'),
        ),
    ]
