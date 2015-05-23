# -*- coding:utf-8 -*-
from django.db import models
from pmo2015.models.bases import BaseModel
from pmo2015.models.user import PmoAdmin


class News(BaseModel):
    class Meta:
        app_label = 'pmo2015'
    content = models.TextField()
    user = PmoAdmin
    email = models.EmailField(null=True)
