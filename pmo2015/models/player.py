from django.db import models

from pmo2015.models.vote import Vote
from tourney.models import BasePlayer


class Player(BasePlayer):
    class Meta:
        app_label = 'pmo2015'

    team = models.CharField(
        help_text='所属队伍',
        max_length=2,
        choices=Vote.TEAM_CHOICES,
        null=False
    )
