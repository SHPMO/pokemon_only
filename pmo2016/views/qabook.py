# coding=utf-8
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.conf import settings
from django.http import HttpResponse
from pmo2016.forms import MessageForm
from pmo2016.views.common import CommonView
from pmo2016.models import MainComment


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
                kwargs["main_comments"] = MainComment.objects.order_by('-gen_time')[l:r]
            except ValueError:
                kwargs["error"] = 2
            total = MainComment.objects.count()
            kwargs.update({
                'comment_number': total,
                'max_page': (total + 4) // 5,
                'form': MessageForm(),
                'contact_email': settings.CONTACT_EMAIL,
                'weibo_url': settings.WEIBO_URL
            })
        return super().get(request, sub, *args, **kwargs)
