# coding=utf-8
from pmo2015.views.common import CommonView
from pmo2015.models import MainComment


class QABookView(CommonView):
    _sub_list = ["faq", "manner", "guestbook"]
    name = "qabook"

    def get(self, request, sub=None, *args, **kwargs):
        if sub == "guestbook":
            try:
                page = kwargs["page"] = int(request.GET.get("page", 1))
                l, r = (page-1) * 5, page * 5
                kwargs["main_comments"] = MainComment.objects.reverse()[l:r]
            except ValueError:
                kwargs["error"] = 2
            kwargs["comment_number"] = MainComment.objects.count()
            kwargs["max_page"] = (kwargs["comment_number"] + 4) // 5
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None, *args, **kwargs):
        nickname = request.POST.get("nickname", "")
        message = request.POST.get("message", "").strip()
        ip_address = request.META.get("REMOTE_ADDR", None)
        if nickname == "" or message == "":
            kwargs["error"] = 1
            kwargs["nickname"] = nickname
            kwargs["message"] = message
        elif ip_address is None:
            kwargs["error"] = -1
        else:
            try:
                MainComment.objects.create(
                    nickname=nickname,
                    content=message,
                    email=request.POST.get("email", None),
                    ip_address=ip_address
                )
                kwargs["error"] = 0
            except:
                kwargs["error"] = -1
        return self.get(request, sub, *args, **kwargs)
