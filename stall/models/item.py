# coding=utf-8
from django.db import models
from stall.models.seller import Seller


class Item(models.Model):
    class Meta:
        app_label = 'stall'

    validated = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller)

    name = models.CharField(max_length=50, default="")
    item_type = models.CharField(max_length=20, default="", help_text="种类")

    content = models.CharField(max_length=100, default="", help_text="内容")
    price = models.FloatField(default=0, help_text="价格")
    url = models.URLField(default="", help_text="链接")
    authors = models.TextField(default="", help_text="作者名单")
    introduction = models.TextField(default="", help_text="简介")

    forto = models.CharField(max_length=20, default="", help_text="面向人群")
    is_restricted = models.CharField(max_length=20, default="", help_text="限制级是否")
    circle = models.CharField(max_length=40, default="", help_text="出品社团")
    is_started_with = models.BooleanField(default=False, help_text="是否首发")

    @classmethod
    def create(cls, seller, **kwargs):
        item = cls.objects.create(
            seller=seller,
            **kwargs
        )
        return item

    def __str__(self):
        return "%s %s" % (self.name, self.seller.circle_name)


class ItemPicture(models.Model):
    class Meta:
        app_label = 'stall'
    picture = models.ImageField(upload_to="items/%Y/%m/%d", max_length=1024, help_text="图片")
    item = models.ForeignKey(Item)

    def __str__(self):
        return "%s %s" % (self.id, self.item.name)

    @classmethod
    def get_default(cls):
        return cls.objects.get(id=1)
