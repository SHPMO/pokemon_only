# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stall', '0002_auto_20180719_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pmo',
            field=models.CharField(max_length=10, help_text='漫展', choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('unknown', 'unknown')], default='unknown'),
        ),
        migrations.AlterField(
            model_name='itempicture',
            name='pmo',
            field=models.CharField(max_length=10, help_text='漫展', choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('unknown', 'unknown')], default='unknown'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pmo',
            field=models.CharField(max_length=10, help_text='漫展', choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('unknown', 'unknown')], default='unknown'),
        ),
        migrations.AlterField(
            model_name='validatecode',
            name='pmo',
            field=models.CharField(max_length=10, help_text='漫展', choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2015', 'pmo2015'), ('pmo2018', 'pmo2018'), ('unknown', 'unknown')], default='unknown'),
        ),
    ]
