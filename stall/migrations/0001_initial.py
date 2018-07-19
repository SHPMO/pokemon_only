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
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pmo', models.CharField(help_text='漫展', choices=[('unknown', 'unknown'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('pmo2017', 'pmo2017'), ('pmo2016', 'pmo2016')], max_length=10, default='unknown')),
                ('validated', models.BooleanField(default=False)),
                ('name', models.CharField(default='未命名', max_length=50)),
                ('item_type', models.CharField(help_text='种类', max_length=20, default='')),
                ('content', models.CharField(help_text='内容', max_length=100, default='')),
                ('price', models.FloatField(help_text='价格', default=0)),
                ('url', models.URLField(help_text='链接', default='')),
                ('authors', models.TextField(help_text='作者名单', default='')),
                ('introduction', models.TextField(help_text='简介', default='')),
                ('cover_image', models.ImageField(null=True, help_text='封面图片', max_length=1024, upload_to='items/%Y/%m/%d')),
                ('forto', models.CharField(help_text='面向人群', max_length=20, default='')),
                ('is_restricted', models.CharField(help_text='限制级是否', max_length=20, default='')),
                ('circle', models.CharField(help_text='出品社团', max_length=40, default='')),
                ('is_started_with', models.BooleanField(help_text='是否首发', default=False)),
                ('item_order', models.IntegerField(help_text='商品排序', default=0)),
            ],
            options={
                'ordering': ['seller'],
            },
        ),
        migrations.CreateModel(
            name='ItemPicture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pmo', models.CharField(help_text='漫展', choices=[('unknown', 'unknown'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('pmo2017', 'pmo2017'), ('pmo2016', 'pmo2016')], max_length=10, default='unknown')),
                ('picture', models.ImageField(help_text='图片', max_length=1024, upload_to='items/%Y/%m/%d')),
                ('item', models.ForeignKey(to='stall.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('key', models.CharField(unique=True, max_length=255)),
                ('value', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pmo', models.CharField(help_text='漫展', choices=[('unknown', 'unknown'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('pmo2017', 'pmo2017'), ('pmo2016', 'pmo2016')], max_length=10, default='unknown')),
                ('email', models.EmailField(max_length=30, verbose_name='email address')),
                ('is_active', models.BooleanField(help_text='是否激活', default=False)),
                ('signup_datetime', models.DateTimeField(auto_now=True)),
                ('signup_address', models.GenericIPAddressField()),
                ('is_stall', models.BooleanField(help_text='是否摊位')),
                ('circle_name', models.CharField(help_text='社团名', max_length=40)),
                ('circle_description', models.TextField(help_text='社团介绍')),
                ('circle_image', models.ImageField(help_text='社团图标', upload_to='circle/%Y/%m/%d')),
                ('seller_id', models.CharField(help_text='摊位号', max_length=10, default='')),
                ('proposer_name', models.CharField(help_text='申请人姓名', max_length=20)),
                ('proposer_sex', models.CharField(help_text='性别', max_length=20)),
                ('proposer_qq', models.CharField(help_text='QQ', max_length=11)),
                ('proposer_phone', models.CharField(help_text='电话', max_length=20)),
                ('proposer_id', models.CharField(help_text='身份证号', max_length=18)),
                ('booth', models.FloatField(help_text='申请摊位数', default=1)),
                ('number_of_people', models.SmallIntegerField(help_text='申请人数', default=1)),
                ('remarks', models.TextField(help_text='备注', default='')),
                ('status', models.IntegerField(help_text='状态')),
                ('notice', models.TextField(help_text='通知', default='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ValidateCode',
            fields=[
                ('pmo', models.CharField(help_text='漫展', choices=[('unknown', 'unknown'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('pmo2017', 'pmo2017'), ('pmo2016', 'pmo2016')], max_length=10, default='unknown')),
                ('code', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('validated', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(to='stall.Seller')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(to='stall.Seller'),
        ),
    ]
