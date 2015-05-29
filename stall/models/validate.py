# coding=utf-8
from django.db import models
from stall.models.bases import BaseStallModel
from stall.models.seller import Seller
import random
import string


class ValidateCode(BaseStallModel):
    code = models.CharField(max_length=20, primary_key=True)
    validated = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller)

    MSTR = string.ascii_letters + string.digits

    def __str__(self):
        return "%s %s" % (self.seller.email, self.code)

    @classmethod
    def create(cls, seller):
        code = ""
        for i in range(20):
            code += random.choice(cls.MSTR)
        if len(cls.objects.filter(code=code)) > 0:
            return cls.create(seller)
        return cls.objects.create(code=code, seller=seller, pmo=seller.pmo)
