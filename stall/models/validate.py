# coding=utf-8
import random
import string

from django.db import models

from stall.models.bases import BaseStallModel
from stall.models.seller import Seller


class ValidateCode(BaseStallModel):
    code = models.CharField(max_length=20, primary_key=True)
    validated = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, models.CASCADE)

    MSTR = string.ascii_letters + string.digits

    def __str__(self):
        return "(%s) %s: %s" % (self.pmo, self.seller.email, self.code)

    @classmethod
    def create(cls, seller):
        code = ""
        for i in range(20):
            code += random.choice(cls.MSTR)
        if cls.objects.filter(code=code).count() > 0:
            return cls.create(seller)
        return cls.objects.create(code=code, seller=seller, pmo=seller.pmo)
