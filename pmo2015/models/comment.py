# -*- coding:utf-8 -*-
from django.db import models
from django.utils.html import escape
from pmo2015.models.bases import BaseModel
from pmo2015.models.user import PmoAdmin


class BaseComment(BaseModel):
    class Meta:
        app_label = 'pmo2015'
        abstract = True
    content = models.TextField()

    def __str__(self):
        return "%s %s" % (self.gen_time.strftime("%c"), self.content[:20])


class MainComment(BaseComment):
    class Meta:
        app_label = 'pmo2015'
    nickname = models.CharField(max_length=30)
    email = models.EmailField(null=True)


class BackComment(BaseComment):
    class Meta:
        app_label = 'pmo2015'
    toward = models.ForeignKey(MainComment)
    admin = models.ForeignKey(PmoAdmin, null=True)
