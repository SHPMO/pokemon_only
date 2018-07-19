# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmo2015', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackComment2016',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('gen_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('admin', models.ForeignKey(to='pmo2015.PmoAdmin', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('gen_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('nickname', models.CharField(max_length=30)),
                ('email', models.EmailField(null=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('taobao_id', models.CharField(max_length=16)),
                ('status', models.SmallIntegerField(default=0)),
                ('signup_time', models.DateTimeField(auto_now=True)),
                ('signup_ip', models.GenericIPAddressField()),
                ('phone', models.CharField(max_length=20)),
                ('receiver_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='backcomment2016',
            name='toward',
            field=models.ForeignKey(to='pmo2016.MainComment'),
        ),
    ]
