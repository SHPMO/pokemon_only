# coding=utf-8
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from stall.models.bases import BaseStallModel


class Seller(BaseStallModel):
    class Meta:
        app_label = "stall"

    user = models.ForeignKey(User)
    email = models.EmailField(
        verbose_name='email address',
        max_length=30,
    )
    is_active = models.BooleanField(default=False, help_text='是否激活')

    signup_datetime = models.DateTimeField(auto_now=True)
    signup_address = models.GenericIPAddressField()

    is_stall = models.BooleanField(help_text='是否摊位')

    circle_name = models.CharField(max_length=40, help_text="社团名")
    circle_description = models.TextField(help_text="社团介绍")
    circle_image = models.ImageField(upload_to="circle/%Y/%m/%d", help_text="社团图标")
    seller_id = models.CharField(max_length=10, default="", help_text='摊位号')
    proposer_name = models.CharField(max_length=20, help_text="申请人姓名")
    proposer_sex = models.CharField(max_length=20, help_text="性别")
    proposer_qq = models.CharField(max_length=11, help_text="QQ")
    proposer_phone = models.CharField(max_length=20, help_text="电话")
    proposer_id = models.CharField(max_length=18, help_text="身份证号")
    booth = models.SmallIntegerField(default=1, help_text="申请摊位数")
    remarks = models.TextField(default='', help_text="备注")

    status = models.IntegerField(help_text="状态")
    notice = models.TextField(default='', help_text="通知")

    def __str__(self):
        return "%s %s" % (self.pmo, self.get_status_string())

    def get_status_string(self):
        if self.status == 0:
            status = '未激活'
        elif self.status == 1:
            status = '未申请'
        elif self.status == 2:
            status = '待审核'
        elif self.status == 3:
            status = '通过'
        elif self.status == 4:
            status = '不通过'
        else:
            status = '未知状态'
        return "%s %s %s" % (status, '摊位' if self.is_stall else '寄卖', self.circle_name)

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
        try:
            seller = cls.objects.create(
                email=email,
                user=user,
                circle_name=circle_name,
                status=0,
                **kwargs
            )
            return seller
        except:
            user.delete()
            raise

    def do_validate(self, passed=True):
        if passed:
            self.status = 3
        else:
            self.status = 4
        self.item_set.update(validated=passed)
        self.save()
