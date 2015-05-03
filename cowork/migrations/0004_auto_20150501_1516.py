# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cowork', '0003_auto_20150424_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=6)),
                ('total_desks', models.IntegerField(verbose_name='Total desks')),
                ('reserved_desks', models.IntegerField(verbose_name='Reserved desks')),
                ('price', models.DecimalField(verbose_name='Price per desk $', max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='office',
            name='company',
        ),
        migrations.RemoveField(
            model_name='room',
            name='office',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='actual_owner',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='color',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='height',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='length',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='number',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='price',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='room',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='until_date',
        ),
        migrations.RemoveField(
            model_name='desk',
            name='width',
        ),
        migrations.AddField(
            model_name='company',
            name='VAT_ID',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='company_logos'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='desk',
            name='owner',
            field=models.OneToOneField(related_name='desks', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Office',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='location',
            name='company',
            field=models.ForeignKey(related_name='locations', to='cowork.Company'),
        ),
        migrations.AddField(
            model_name='desk',
            name='location',
            field=models.OneToOneField(related_name='desks', default='', to='cowork.Location'),
        ),
    ]
