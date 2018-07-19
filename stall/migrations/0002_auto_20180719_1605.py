# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pmo',
            field=models.CharField(default='unknown', help_text='漫展', max_length=10, choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2018', 'pmo2018'), ('pmo2015', 'pmo2015'), ('unknown', 'unknown')]),
        ),
        migrations.AlterField(
            model_name='itempicture',
            name='pmo',
            field=models.CharField(default='unknown', help_text='漫展', max_length=10, choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2018', 'pmo2018'), ('pmo2015', 'pmo2015'), ('unknown', 'unknown')]),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pmo',
            field=models.CharField(default='unknown', help_text='漫展', max_length=10, choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2018', 'pmo2018'), ('pmo2015', 'pmo2015'), ('unknown', 'unknown')]),
        ),
        migrations.AlterField(
            model_name='validatecode',
            name='pmo',
            field=models.CharField(default='unknown', help_text='漫展', max_length=10, choices=[('pmo2016', 'pmo2016'), ('pmo2017', 'pmo2017'), ('pmo2018', 'pmo2018'), ('pmo2015', 'pmo2015'), ('unknown', 'unknown')]),
        ),
    ]
