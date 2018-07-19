# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pmo2015.models.user


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('gen_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
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
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('gen_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'news',
            },
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
                ('team', models.CharField(help_text='所属队伍', choices=[('AQ', '水舰队'), ('MG', '熔岩团')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PmoAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('pmo', models.CharField(help_text='漫展', choices=[('unknown', 'unknown'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('pmo2017', 'pmo2017'), ('pmo2016', 'pmo2016')], max_length=10, default='unknown')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('gen_time', models.DateTimeField(auto_now=True)),
                ('choice', models.CharField(help_text='选择', choices=[('AQ', '水舰队'), ('MG', '熔岩团')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(to='pmo2015.PmoAdmin', default=pmo2015.models.user.PmoAdmin.get_default_admin),
        ),
        migrations.AddField(
            model_name='backcomment',
            name='admin',
            field=models.ForeignKey(to='pmo2015.PmoAdmin', null=True),
        ),
        migrations.AddField(
            model_name='backcomment',
            name='toward',
            field=models.ForeignKey(to='pmo2015.MainComment'),
        ),
    ]
