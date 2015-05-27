# coding=utf-8
from django.db import models


class BaseStallModel(models.Model):
    class Meta:
        app_label = 'stall'
        abstract = True

    PMO_CHOICES = (
        ('unknown', 'unknown'),
        ('pmo2015', 'pmo2015')
    )
    pmo = models.CharField(max_length=10, default='unknown', choices=PMO_CHOICES, help_text="漫展")
