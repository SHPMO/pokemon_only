from django.db import models
from django.utils.html import escape


class BasePlayer(models.Model):
    class Meta:
        app_label = 'tourney'
        abstract = True
    player_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    taobao_id = models.CharField(max_length=50)
    status = models.SmallIntegerField(default=0)
    signup_time = models.DateTimeField(auto_now=True)
    signup_ip = models.GenericIPAddressField()

    def __str__(self):
        if self.status == 0:
            x = '待审'
        elif self.status == 1:
            x = '通过'
        else:
            x = '拒绝'
        return "%s %s %s" % (x, self.player_name, self.email)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def do_validate(self, passed=True):
        if passed:
            self.status = 1
        else:
            self.status = 2

