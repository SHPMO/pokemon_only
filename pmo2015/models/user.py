# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class PmoAdmin(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=30)
