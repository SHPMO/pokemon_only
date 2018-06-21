# coding=utf-8
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.template import loader
from dashboard.views.common import CommonView
from stall.models import Seller


class AdminView(CommonView):
    _sub_list = ["default", 'stall', 'login', 'info']
    name = "admin"
    admin = None

    def _init(self, request):
        if not (request.user.is_authenticated() and any(request.user.groups.filter(name='PmoAdminGroup'))):
            raise Http404
        # self.admin = request.user.pmoadmin_set.get(pmo='pmo2018')
        self.admin = request.user.pmoadmin_set.first()

    def _default(self):
        return redirect("dashboard:admin")

    def _info_get(self, request, kwargs):
        kwargs.update({
            'admin': self.admin
        })

    def _info_post(self, request):
        pwd = request.POST.get('password')
        ncn = request.POST.get('nickname')
        if pwd:
            self.admin.user.set_password(pwd)
            self.admin.user.save()
        if ncn:
            self.admin.nickname = ncn
            self.admin.save()
        return redirect("dashboard:admin", sub='info')

    def _stall_get(self, request, kwargs):
        current = Seller.objects.filter(pmo=self.pmo, pk=request.GET.get('seller_id'))
        if current.count() == 1:
            current = current[0]
        else:
            current = None
        kwargs.update({
            'current': current,
            'sellers': Seller.objects.filter(pmo=self.pmo)
        })

    def _stall_post(self, request):
        me = request.POST.get('submit')
        current = Seller.objects.filter(pmo=self.pmo, pk=request.POST.get('seller_id'))
        if current.count() != 1:
            raise Http404
        current = current[0]
        if me == 'notice':
            notice = request.POST.get('notice')
            if notice:
                current.notice = notice
                current.save()
                if request.POST.get('send_email') == 'send':
                    send_mail(
                        '%s%s通知' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
                        settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
                        html_message=loader.get_template('dashboard/mails/seller_notice.html').render({
                            'seller': current, 'base_url': settings.BASE_URL,
                        })
                    )
            response = redirect("dashboard:admin", sub='stall')
            response['Location'] += '?seller_id=%s' % current.pk
            return response
        elif me == 'accept':
            current.do_validate(True)
        elif me == 'reject':
            current.do_validate(False)
        elif me == 'setid':
            seller_id = request.POST.get('sellerid')
            if seller_id:
                current.seller_id = seller_id
                current.save()
                if request.POST.get('send_email') == 'send':
                    send_mail(
                        '%s%s通知' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
                        settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
                        html_message=loader.get_template('dashboard/mails/seller_sellerid.html').render({
                            'seller': current, 'base_url': settings.BASE_URL,
                        })
                    )
            response = redirect("dashboard:admin", sub='stall')
            response['Location'] += '?seller_id=%s' % current.pk
            return response
        else:
            raise Http404
        send_mail(
            '%s%s申请结果' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
            settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
            html_message=loader.get_template('dashboard/mails/seller_validated.html').render({
                'seller': current, 'base_url': settings.BASE_URL,
                'message': request.POST.get('message', '')
            })
        )
        response = redirect("dashboard:admin", sub='stall')
        response['Location'] += '?seller_id=%s' % current.pk
        return response

    def get(self, request, sub=None, *args, **kwargs):
        if sub == 'login':
            if request.GET.get('fail') == '1':
                kwargs['fail'] = True
            return super().get(request, sub, *args, **kwargs)
        self._init(request)
        if sub == 'logout':
            logout(request)
            return self._default()
        if sub == 'default':
            raise Http404
        if sub is None:
            sub = 'default'
        kwargs.update({
            'admin': self.admin
        })
        if sub == 'info':
            self._info_get(request, kwargs)
        elif sub == 'stall':
            self._stall_get(request, kwargs)
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None):
        if sub == 'login':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is None or not any(user.groups.filter(name='PmoAdminGroup')):
                response = redirect("dashboard:admin", sub='login')
                response['Location'] += '?fail=1'
                return response
            login(request, user)
            return self._default()
        self._init(request)
        if sub == 'info':
            return self._info_post(request)
        elif sub == 'stall':
            return self._stall_post(request)
        else:
            raise Http404
