from django.db import models
from tourney.models import BasePlayer


class Player(BasePlayer):
    class Meta:
        app_label = 'pmo2016'

    phone = models.CharField(max_length=20, null=False)
    receiver_name = models.CharField(max_length=40, null=False)
