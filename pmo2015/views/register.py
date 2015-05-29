# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from pmo2015.views.common import CommonView
from stall.forms import LoginForm, SignupForm
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign", "signupin", "wrong"]
    _err_dict = {
        "1": "邮箱已通过验证，请登录",
        "2": "注销成功"
    }
    name = "register"

    def get(self, request, sub=None, *args, **kwargs):
        if request.GET.get('newsn') == '1':
            csn = CaptchaStore.generate_key()
            cimageurl = captcha_image_url(csn)
            return HttpResponse(cimageurl)
        if sub == 'wrong':
            raise Http404
        if sub in {'stall', 'consign'}:
            if not request.user.is_authenticated():
                return redirect("pmo2015:register", sub='signupin')
            if request.user.seller.is_stall == (sub == 'stall'):
                sub = 'stall'
                kwargs.update({
                    'seller': request.user.seller,
                    'page': int(request.GET.get('page', 0)),
                })
            else:
                is_stall = sub == 'stall'
                kwargs.update({
                    'is_stall': is_stall,
                    'correct_url': reverse('pmo2015:register', kwargs={'sub': 'consign' if is_stall else 'stall'})
                })
                sub = 'wrong'
        elif sub == 'signupin':
            kwargs.update({
                'login_form': LoginForm(),
                'signup_form': SignupForm(),
                'f': request.GET.get('f', None) == 'login',
                'error_message': self._err_dict.get(request.GET.get('validated', None), "")
            })
        return super().get(request, sub, *args, **kwargs)
