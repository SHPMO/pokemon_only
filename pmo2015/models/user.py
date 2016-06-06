from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class PmoAdmin(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=30)
    PMO_CHOICES = tuple(
        (x, x)
        for x in settings.PMO_LIST
    )
    pmo = models.CharField(max_length=10, default='unknown', choices=PMO_CHOICES, help_text="漫展")

    @classmethod
    def create(cls, username, email, password, *args, **kwargs):
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.groups = [Group.objects.get_or_create(name="PmoAdminGroup")[0]]
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
