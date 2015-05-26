# coding=utf-8
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class PmoAdmin(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=30)

    @classmethod
    def create(cls, username, email, password, *args, **kwargs):
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        group = Group.objects.get(name="PMOAdminGroup")
        user.groups.add(group)
        user.save()
        return cls.objects.create(
            nickname=username,
            user=user
        )
