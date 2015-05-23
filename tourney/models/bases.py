from django.db import models


class BasePlayer(models.Model):
    class Meta:
        app_label = 'tourney'
        abstract = True
    player_id = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    taobao_id = models.CharField(max_length=20)
    validated = models.BooleanField(default=False)
    signup_time = models.DateTimeField(auto_now=True)
    signup_ip = models.GenericIPAddressField()
