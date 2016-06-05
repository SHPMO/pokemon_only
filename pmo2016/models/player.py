from django.db import models
from tourney.models import BasePlayer


class Player(BasePlayer):
    class Meta:
        app_label = 'pmo2016'
