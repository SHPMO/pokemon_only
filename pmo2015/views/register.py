# coding=utf-8
from pmo2015.views.common import CommonView


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign", "signupin"]
    name = "register"

    def get(self, request, sub=None, *args, **kwargs):
        if sub in {'stall', 'consign'}:
            sub = 'stall'
            if not request.user.is_authenticated():
                sub = "signupin"

        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None, *args, **kwargs):
        pass
