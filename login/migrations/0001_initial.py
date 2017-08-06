# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delete_flag', models.CharField(max_length=4, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe5\xbf\x97')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, verbose_name=b'\xe7\x99\xbb\xe5\x85\xa5\xe5\x90\x8d')),
                ('passwd', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('delete_flag', models.CharField(max_length=4, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe5\xbf\x97')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('Name', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
                ('description', models.TextField(verbose_name=b'\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            bases=('login.basemodel',),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('Name', models.CharField(max_length=32, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.TextField(verbose_name=b'\xe6\x9d\x83\xe9\x99\x90\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            bases=('login.basemodel',),
        ),
        migrations.CreateModel(
            name='User_Group',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('userID', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7 id')),
                ('groupID', models.IntegerField(verbose_name=b'\xe7\xbb\x84 id')),
            ],
            bases=('login.basemodel',),
        ),
        migrations.CreateModel(
            name='User_Permission',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='login.BaseModel')),
                ('userID', models.IntegerField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7 id')),
                ('groupID', models.IntegerField(verbose_name=b'\xe7\xbb\x84 id')),
            ],
            bases=('login.basemodel',),
        ),
    ]
