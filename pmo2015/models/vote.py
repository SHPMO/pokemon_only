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

    def __str__(self):
        return '%s %s' % (self.TEAM_CHOICES[0][1] if self.choice == self.TEAM_AQUA else self.TEAM_CHOICES[1][1], self.gen_time)
