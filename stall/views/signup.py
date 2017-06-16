from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, loader
from django.utils.datastructures import MultiValueDictKeyError
from stall.views.bases import ApiView, View
from stall.models import Seller, ValidateCode
from stall.forms import LoginForm, SignupForm


class SignupView(ApiView):
    @staticmethod
    def send_validate_mail(seller, validate_code):
        send_mail(
            '%s PMO 摊位用户激活邮件' % settings.EMAIL_SUBJECT_PREFIX, "",
            settings.EMAIL_HOST_USER, [seller.email], fail_silently=False,
            html_message=loader.get_template('stall/validate_email.html').render({
                'validate_code': validate_code.code, 'base_url': settings.BASE_URL
            }),
        )

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
        s_seller = Seller.objects.filter(email=signup.cleaned_data['email'], pmo=signup.cleaned_data['pmo'])
        if s_seller.count() > 0:
            if s_seller[0].is_active:
                return self.return_me(2, "该Email已被注册。")
            else:
                validate_code = ValidateCode.objects.get(seller=s_seller[0])
                self.send_validate_mail(s_seller[0], validate_code)
                return self.return_me(6, "已重新发送激活邮件，请前往邮箱查收。")
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
            return self.return_me()

        validate_code = ValidateCode.create(seller=seller)
        self.send_validate_mail(seller, validate_code)
        return self.return_me(0, "注册成功，请前往邮箱查收激活邮件。")


class ValidateView(View):
    # TODO: send a success mail.
    # @staticmethod
    # def send_success_mail(seller, validate_code):
    #     send_mail()

    @staticmethod
    def get(request, *args, **kwargs):
        try:
            vc = ValidateCode.objects.get(code=request.GET["validate_code"])
        except MultiValueDictKeyError:
            raise Http404
        except ValidateCode.DoesNotExist:
            raise Http404
        if vc.seller.is_active:
            return HttpResponse("请勿重复激活邮箱。")
        vc.seller.is_active = vc.validated = True
        vc.seller.status = 1
        vc.save()
        vc.seller.save()
        response = redirect("%s:register" % vc.pmo, sub='signupin')
        response['Location'] += '?validated=1#login'
        return response
