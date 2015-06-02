from django.db import models
from tourney.models import BasePlayer
from pmo2015.models.vote import Vote


class Player(BasePlayer):
    class Meta:
        app_label = 'pmo2015'
    team = models.CharField(
        help_text='所属队伍',
        max_length=2,
        choices=Vote.TEAM_CHOICES,
        null=False
    )
