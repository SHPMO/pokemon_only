# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from stall.models.bases import BaseStallModel


class Seller(BaseStallModel):
    class Meta:
        app_label = "stall"

    user = models.OneToOneField(User)
    email = models.EmailField(
        verbose_name='email address',
        max_length=30,
        unique=True,
    )
    is_active = models.BooleanField(default=False, help_text='是否激活')
    validated = models.BooleanField(default=False, help_text='是否通过')

    signup_datetime = models.DateTimeField(auto_now=True)
    signup_address = models.GenericIPAddressField()

    is_stall = models.BooleanField('是否摊位')

    circle_name = models.CharField(max_length=40, help_text="社团名")
    circle_description = models.TextField(help_text="社团介绍")
    circle_image = models.ImageField(upload_to="circle/%Y/%m/%d", help_text="社团图标")
    proposer_name = models.CharField(max_length=20, help_text="申请人姓名")
    proposer_sex = models.CharField(max_length=20, help_text="性别")
    proposer_qq = models.CharField(max_length=11, help_text="QQ")
    proposer_phone = models.CharField(max_length=20, help_text="电话")
    proposer_id = models.CharField(max_length=18, help_text="身份证号")
    booth = models.SmallIntegerField(default=0, help_text="申请摊位数")
    remarks = models.TextField(help_text="备注")

    def __str__(self):
        return "%s %s" % (self.circle_name, self.email)

    @classmethod
    def create_seller(cls, email, circle_name, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        if not circle_name:
            raise ValueError('Users must have a circle name')
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        seller = cls.objects.create(
            email=email,
            user=user,
            circle_name=circle_name,
            **kwargs
        )
        return seller
