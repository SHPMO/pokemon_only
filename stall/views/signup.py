from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from stall.views.bases import ApiView, View
from stall.models import Seller, ValidateCode
from stall.forms import LoginForm, SignupForm


class SignupView(ApiView):
    def post(self, request, *args, **kwargs):
        signup = SignupForm(request.POST)
        if not signup.is_valid():
            return self.return_me(1, signup.errors)
        if signup.cleaned_data['password'] != signup.cleaned_data['repassword']:
            return self.return_me(3, "两次输入密码不一样。")
        if signup.cleaned_data['type'] == "stall":
            is_stall = True
        elif signup.cleaned_data['type'] == "consign":
            is_stall = False
        else:
            return self.return_me(4, "请选择类型。")
        if signup.cleaned_data['pmo'] not in Seller.PMO_LIST:
            return self.return_me(5, "非法请求。")
        if len(Seller.objects.filter(email=signup.cleaned_data['email'])) > 0:
            return self.return_me(2, "该Email已被注册。")
        try:
            seller = Seller.create_seller(
                email=signup.cleaned_data['email'],
                circle_name=signup.cleaned_data['circle_name'],
                password=signup.cleaned_data['password'],
                is_stall=is_stall,
                signup_address=request.META['REMOTE_ADDR'],
                pmo=signup.cleaned_data['pmo']
            )
        except:
            return self.return_me(-1, "未知错误。")

        validate_code = ValidateCode.create(seller=seller)
        send_mail(
            '%sPMO摊位/寄卖用户激活邮件' % settings.EMAIL_SUBJECT_PREFIX,
            '%s' % validate_code.code, settings.EMAIL_HOST_USER, [seller.email], fail_silently=False)
        return self.return_me(0, "注册成功，请前往邮箱查收激活邮件。")


class ValidateView(View):
    def get(self, request, validate_code, *args, **kwargs):
        vc = ValidateCode.objects.get(code=validate_code)
        if vc.validated:
            return HttpResponse("请勿重复激活邮箱。")
        return redirect("%s:register" % vc.pmo, {'sub': 'stall'})
