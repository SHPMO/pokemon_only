from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from stall.views.bases import ApiView, View
from stall.models import Seller, ValidateCode


class SignupView(ApiView):
    def post(self, request, *args, **kwargs):
        data = {
            "email": request.POST.get('email', None),
            "circle_name": request.POST.get('circle_name', None),
            "password": request.POST.get('password', None),
            "is_stall": request.POST.get('is_stall', None),
            "signup_address": request.META.get('REMOTE_ADDR', None),
            "pmo": request.META.get('pmo', None)
        }
        if not all(data.values()):
            return self.return_me(1, "所有信息均为必填。")
        if len(Seller.objects.filter(email=data["email"])) > 0:
            return self.return_me(2, "该Email已被注册。")
        try:
            seller = Seller.create_seller(**data)
        except:
            return self.return_me(-1, "未知错误。")
        validate_code = ValidateCode.create(seller=seller)
        send_mail('PMO摊位/寄卖用户激活邮件', '%s' % validate_code, settings.EMAIL_HOST_USER, [seller.email], fail_silently=False)
        return self.return_me(0, "注册成功，请前往邮箱查收激活邮件。")


class ValidateView(View):
    def get(self, request, validate_code, *args, **kwargs):
        vc = ValidateCode.objects.get(code=validate_code)
        if vc.validated:
            return HttpResponse("请勿重复激活邮箱。")
        return redirect("%s:register" % vc.pmo, {'sub': 'stall'})
