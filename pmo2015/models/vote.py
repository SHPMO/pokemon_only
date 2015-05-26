# -*- coding:utf-8 -*-
from pmo2015.models.bases import BaseModel
from django.db import models


class Vote(BaseModel):
    class Meta:
        app_label = 'pmo2015'
    TEAM_AQUA = 'AQ'
    TEAM_MAGMA = 'MG'
    TEAM_CHOICES = (
        (TEAM_AQUA, '水舰队'),
        (TEAM_MAGMA, '熔岩团'),
    )
    choice = models.CharField(
        help_text='选择',
        max_length=2,
        choices=TEAM_CHOICES,
        null=False
    )
