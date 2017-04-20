# coding=utf-8
from django.views.generic import View
from django.http import Http404, HttpResponse
import json


class ApiView(View):
    seller = None
    pmo = None

    def get(self, request):
        raise Http404

    def return_me(self, error_code=-1, message=None, **kwargs):
        if message is None:
            message = '未知错误'
        data = {'error': error_code, 'message': message}
        data.update(kwargs)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        if self.seller:
            response.set_cookie('status', self.seller.status)
        return response


class AuthedApiView(ApiView):
    def post(self, request, cancel=True, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404
        pmo = request.POST.get('pmo')
        seller = request.user.seller_set.filter(pmo=pmo)
        cs = seller.count()
        if cs == 0:
            return self.return_me(-2, '不存在该用户')
        elif cs > 1:
            return self.return_me()
        self.pmo = pmo
        self.seller = seller[0]
        if cancel and self.seller.status != 1:
            return self.return_me(-3, '现在无法编辑')
        return None
