from django.db import models
from django.utils.html import escape


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

    def __str__(self):
        return "%s %s" % (self.player_id, self.email)

    @classmethod
    def create(cls, *args, **kwargs):
        assert len(kwargs['player_id']) <= 30
        assert len(kwargs['taobao_id']) <= 20
        return cls.objects.create(*args, **kwargs)
