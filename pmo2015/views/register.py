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
        if sub == 'signupin':
            kwargs.update({
                'login_form': LoginForm(),
                'signup_form': SignupForm()
            })
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None, *args, **kwargs):
        pass
