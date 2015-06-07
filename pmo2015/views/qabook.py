# coding=utf-8
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.http import HttpResponse
from pmo2015.forms import MessageForm
from pmo2015.views.common import CommonView
from pmo2015.models import MainComment


class QABookView(CommonView):
    _sub_list = ["faq", "manner", "guestbook"]
    name = "qabook"

    def get(self, request, sub=None, *args, **kwargs):
        if sub == "guestbook":
            if request.GET.get('newsn') == '1':
                csn = CaptchaStore.generate_key()
                cimageurl = captcha_image_url(csn)
                return HttpResponse(cimageurl)
            try:
                page = kwargs["page"] = int(request.GET.get("page", 1))
                l, r = (page-1) * 5, page * 5
                kwargs["main_comments"] = MainComment.objects.reverse()[l:r]
            except ValueError:
                kwargs["error"] = 2
            kwargs["comment_number"] = MainComment.objects.count()
            kwargs["max_page"] = (kwargs["comment_number"] + 4) // 5
            kwargs["form"] = MessageForm()
        return super().get(request, sub, *args, **kwargs)
