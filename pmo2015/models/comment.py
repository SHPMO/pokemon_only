# -*- coding:utf-8 -*-
from django.db import models
from pmo2015.models.bases import BaseModel


class BaseComment(BaseModel):
    class Meta:
        app_label = 'pmo2015'
        abstract = True
    nickname = models.CharField(max_length=30)
    content = models.TextField()


class MainComment(BaseComment):
    class Meta:
        app_label = 'pmo2015'


class BackComment(BaseComment):
    class Meta:
        app_label = 'pmo2015'
    toward = models.OneToOneField(MainComment)
