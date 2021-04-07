# codin=utf-8
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

from dashboard.views.common import CommonView
from stall.forms import LoginForm, SignupForm
from stall.models import Item


class RegisterView(CommonView):
    _sub_list = ["stall", "signupin"]
    _err_dict = {
        "1": "邮箱已通过验证，请登录",
        "2": "注销成功"
    }
    name = "register"

    def _get_items(self, seller, page=1):
        if page <= 1:
            page = 1
        else:
            a = Item.objects.filter(seller=seller, pmo=self.pmo).count()
            if page > (a + 4) // 5:
                page = (a + 4) // 5
        items = Item.objects.filter(seller=seller, pmo=self.pmo).order_by("item_order")[page * 5 - 5:page * 5]
        ret = []
        for i in range(items.count()):
            ret.append((page * 5 - 4 + i, items[i]))
        for i in range(items.count(), 5):
            ret.append((page * 5 - 4 + i, None))
        return ret, page

    @staticmethod
    def _get_images(item):
        images = item.itempicture_set.all()
        ret = []
        for i in range(images.count()):
            ret.append((i + 1, images[i].picture.url, images[i].pk))
        for i in range(images.count(), 5):
            ret.append((i + 1, None, None))
        return ret

    def get(self, request, sub=None, *args, **kwargs):
        if request.GET.get('newsn') == '1':
            csn = CaptchaStore.generate_key()
            cimageurl = captcha_image_url(csn)
            return HttpResponse(cimageurl)
        if sub == 'wrong':
            raise Http404
        if sub == 'stall':
            if not request.user.is_authenticated:
                return redirect("dashboard:register", sub='signupin')
            seller = request.user.seller_set.filter(pmo=self.pmo)
            if seller.count() != 1:
                return redirect("dashboard:register", sub='signupin')
            seller = seller[0]
            if 'item_id' in request.GET:
                item_id = request.GET['item_id']
                item = Item.objects.filter(pk=item_id, pmo=self.pmo, seller=seller)
                if item.count() == 1:
                    return render(
                        request,
                        'dashboard/register/stall/itemform.html',
                        {
                            'item': item[0],
                            'images': self._get_images(item[0]),
                            'pmo': self.pmo
                        }
                    )
                else:
                    return HttpResponse("")
            if 'page' in request.GET:
                try:
                    page = int(request.GET['page'])
                except ValueError:
                    raise Http404
                items, page = self._get_items(seller, page)
                return render(request, 'dashboard/register/stall/itemtable.html', {
                    'items': items,
                    'page': page
                })
            is_stall = sub == 'stall'
            if seller.is_stall == is_stall:
                sub = 'stall'
                items, page = self._get_items(seller)
                kwargs.update({
                    'seller': seller,
                    'items': items,
                    'page': page,
                })
            else:
                kwargs.update({
                    'is_stall': is_stall,
                    'correct_url': reverse('dashboard:register', kwargs={'sub': 'consign' if is_stall else 'stall'})
                })
                sub = 'wrong'
        elif sub == 'signupin':
            kwargs.update({
                'login_form': LoginForm(),
                'signup_form': SignupForm(),
                'error_message_login': self._err_dict.get(request.GET.get('validated', None), "")
            })
        return super().get(request, sub, *args, **kwargs)
