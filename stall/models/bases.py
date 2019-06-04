# coding=utf-8
from django.conf import settings
from django.db import models


class BaseStallModel(models.Model):
    class Meta:
        app_label = 'stall'
        abstract = True

    PMO_CHOICES = tuple(
        (x, x)
            for x in settings.PMO_LIST
    )
    pmo = models.CharField(max_length=10, default='unknown', choices=PMO_CHOICES, help_text="漫展")


class Option(models.Model):
    class Meta:
        app_label = 'stall'

    key = models.CharField(unique=True, max_length=255)
    value = models.TextField(default="")
