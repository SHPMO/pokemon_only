# coding=utf-8
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class PmoAdmin(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=30)

    @classmethod
    def create(cls, username, email, password, *args, **kwargs):
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.groups = [Group.objects.get_or_create(name="Pmo2015AdminGroup")[0]]
        user.save()
        return cls.objects.create(
            nickname=username,
            user=user
        )

    @staticmethod
    def get_default_admin():
        return PmoAdmin.objects.first()

    def __str__(self):
        return "%s" % self.nickname
