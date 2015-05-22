# coding=utf-8
from django.db import models


class BaseModel(models.Model):
    class Meta:
        app_label = 'pmo2015'
        abstract = True
    ip_address = models.GenericIPAddressField()
    gen_time = models.DateTimeField(
        '投票时间',
        auto_now=True
    )

