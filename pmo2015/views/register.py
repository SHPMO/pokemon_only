# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from pmo2015.views.common import CommonView
from stall.forms import LoginForm, SignupForm
from stall.models import Item
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign", "signupin", "wrong"]
    _err_dict = {
        "1": "邮箱已通过验证，请登录",
        "2": "注销成功"
    }
    name = "register"

    @staticmethod
    def _get_items(seller, page=1):
        items = Item.objects.filter(seller=seller, pmo='pmo2015')[page*5-5:page*5]
        ret = []
        for i in range(len(items)):
            ret.append((page*5 - 4 + i, items[i]))
        for i in range(len(items), 5):
            ret.append((page*5 - 4 + i, None))
        return ret

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
            seller = request.user.seller_set.filter(pmo='pmo2015')
            if len(seller) != 1:
                return redirect("pmo2015:register", sub='signupin')
            seller = seller[0]
            if 'item_id' in request.GET:
                item_id = request.GET['item_id']
                item = Item.objects.filter(pk=item_id, pmo='pmo2015', seller=seller)
                if len(item) == 1:
                    return render(request, 'pmo2015/register/stall/itemform.html', {'item': item[0]})
                else:
                    return HttpResponse("")
            if 'page' in request.GET:
                page = int(request.GET['page'])
                return render(request, 'pmo2015/register/stall/itemtable.html', {
                    'items': self._get_items(seller, page),
                    'total': Item.objects.filter(seller=seller, pmo='pmo2015').count()
                })
            is_stall = sub == 'stall'
            if seller.is_stall == is_stall:
                sub = 'stall'
                kwargs.update({
                    'seller': seller,
                    'items': self._get_items(seller),
                    'total': Item.objects.filter(seller=seller, pmo='pmo2015').count()
                })
            else:
                kwargs.update({
                    'is_stall': is_stall,
                    'correct_url': reverse('pmo2015:register', kwargs={'sub': 'consign' if is_stall else 'stall'})
                })
                sub = 'wrong'
        elif sub == 'signupin':
            kwargs.update({
                'login_form': LoginForm(),
                'signup_form': SignupForm(),
                'error_message': self._err_dict.get(request.GET.get('validated', None), "")
            })
        return super().get(request, sub, *args, **kwargs)
