# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rent_start_date', models.DateTimeField(null=True)),
                ('rent_end_date', models.DateTimeField(null=True)),
                ('number', models.IntegerField()),
                ('width', models.IntegerField()),
                ('length', models.IntegerField()),
                ('height', models.IntegerField()),
                ('color', models.IntegerField()),
                ('price', models.IntegerField()),
                ('actual_owner', models.OneToOneField(related_name='desk', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('company', models.ForeignKey(related_name='offices', to='cowork.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('metrage', models.IntegerField()),
                ('office', models.ForeignKey(related_name='rooms', to='cowork.Office')),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='room',
            field=models.ForeignKey(related_name='desks', to='cowork.Room'),
        ),
    ]
