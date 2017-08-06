# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('Hostname', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('Mac', models.CharField(max_length=32, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('Ip', models.CharField(max_length=32, verbose_name=b'IP')),
                ('Cpu', models.CharField(max_length=32, verbose_name=b'cpu')),
                ('Mem', models.CharField(max_length=32, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('Disk', models.CharField(max_length=32, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98')),
                ('IO', models.CharField(max_length=32, verbose_name=b'\xe8\xaf\xbb\xe5\x86\x99')),
                ('LastLogin', models.DateTimeField(max_length=32, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('LastLoginUser', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\x85\xa5\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7')),
                ('isActive', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xa2\xab\xe6\xbf\x80\xe6\xb4\xbb')),
            ],
            bases=('login.basemodel',),
        ),
        migrations.CreateModel(
            name='UserServer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('userID', models.IntegerField()),
                ('serId', models.IntegerField()),
            ],
            bases=('login.basemodel',),
        ),
    ]
