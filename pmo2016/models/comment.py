from django.db import models
from django.utils.html import escape
from pmo2016.models.bases import BaseModel
from pmo2015.models.user import PmoAdmin


class BaseComment(BaseModel):
    class Meta:
        app_label = 'pmo2016'
        abstract = True
    content = models.TextField()

    def __str__(self):
        return "%s %s" % (self.gen_time.strftime("%c"), self.content[:20])


class MainComment(BaseComment):
    class Meta:
        app_label = 'pmo2016'
    nickname = models.CharField(max_length=30)
    email = models.EmailField(null=True)


class BackComment2016(BaseComment):
    class Meta:
        app_label = 'pmo2016'
    toward = models.ForeignKey(MainComment)
    admin = models.ForeignKey(PmoAdmin, null=True)
