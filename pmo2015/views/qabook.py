# coding=utf-8
from pmo2015.views.common import CommonView
from pmo2015.models import MainComment, BackComment


class QABookView(CommonView):
    _sub_list = ["faq", "manner", "guestbook"]
    name = "qabook"

    def get(self, request, sub=None, page=None, *args, **kwargs):
        if sub == "guestbook":
            if page is None:
                page = 1
            l, r = (page-1) * 10, page * 10
            kwargs["mainComments"] = MainComment.objects.reverse()[l:r]
            kwargs["backComments"] = [
                each.backcomment
                for each in kwargs["mainComments"]
                if each.backcomment is not None
            ]
        return super().get(request, sub, page, *args, **kwargs)
