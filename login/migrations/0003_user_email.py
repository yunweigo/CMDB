# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_server_userserver'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2017, 7, 19, 12, 38, 1, 721000, tzinfo=utc), max_length=64),
            preserve_default=False,
        ),
    ]
