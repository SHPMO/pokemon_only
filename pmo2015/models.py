# coding=utf-8
from django.db import models
from tourney.models import BasePlayer


class Vote(models.Model):
    TEAM_AQUA = 'AQ'
    TEAM_MAGMA = 'MG'
    TEAM_CHOICES = (
        (TEAM_AQUA, '水舰队'),
        (TEAM_MAGMA, '熔岩团'),
    )
    choice = models.CharField(
        '选择',
        max_length=2,
        choices=TEAM_CHOICES,
        null=False
    )
    vote_time = models.DateTimeField(
        '投票时间',
        auto_now=True
    )
    vote_address = models.GenericIPAddressField()


class Player(BasePlayer):
    team = models.CharField(
        '所属队伍',
        max_length=2,
        choices=Vote.TEAM_CHOICES,
        null=False
    )
