# coding=utf-8
from django.db import models
from django.utils.html import escape


class BaseModel(models.Model):
    class Meta:
        app_label = 'pmo2016'
        abstract = True
    ip_address = models.GenericIPAddressField()
    gen_time = models.DateTimeField(
        auto_now=True
    )

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

