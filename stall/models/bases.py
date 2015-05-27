# coding=utf-8
from django.db import models


class BaseStallModel(models.Model):
    class Meta:
        app_label = 'stall'
        abstract = True

    PMO_LIST = ['unknown', 'pmo2015']
    PMO_CHOICES = tuple(
        (x, x)
        for x in PMO_LIST
    )
    pmo = models.CharField(max_length=10, default='unknown', choices=PMO_CHOICES, help_text="漫展")
