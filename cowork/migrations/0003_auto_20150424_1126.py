# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0002_auto_20150424_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 22, 668518, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desk',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 28, 436917, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 37, 32957, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 41, 883406, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 47, 133269, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 11, 26, 51, 242119, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
