# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import redirect
from pmo2015.views.common import CommonView
from stall.forms import LoginForm, SignupForm
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign", "signupin"]
    name = "register"

    def get(self, request, sub=None, *args, **kwargs):
        if request.GET.get('newsn') == '1':
            csn = CaptchaStore.generate_key()
            cimageurl = captcha_image_url(csn)
            return HttpResponse(cimageurl)
        if sub in {'stall', 'consign'}:
            sub = 'stall'
            if not request.user.is_authenticated():
                return redirect("pmo2015:register", sub='signupin')
            kwargs.update({
                'seller': request.user.seller,
                'page': int(request.GET.get('page', 0)),
            })
        elif sub == 'signupin':
            kwargs.update({
                'login_form': LoginForm(),
                'signup_form': SignupForm(),
                'f': request.GET.get('f', None) == 'login',
                'error_message': "邮箱已通过验证，请登录" if request.GET.get('validated', None) == "1" else ""
            })
        return super().get(request, sub, *args, **kwargs)
