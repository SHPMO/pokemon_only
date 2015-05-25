# coding=utf-8
from pmo2015.views.common import CommonView
from pmo2015.models import Player, Vote
import random


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign"]
    name = "register"

    def get(self, request, sub=None, *args, **kwargs):
        return super().get(request, sub, *args, **kwargs)
