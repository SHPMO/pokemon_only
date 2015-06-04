# coding=utf-8
from django.views.generic import View
from django.http import Http404, HttpResponse
import json


class ApiView(View):
    seller = None
    pmo = None

    def get(self, request):
        raise Http404

    @staticmethod
    def return_me(error_code, message=None, **kwargs):
        response = {'error': error_code, 'message': message}
        response.update(kwargs)
        return HttpResponse(json.dumps(response), content_type='application/json')


class AuthedApiView(ApiView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404
        pmo = request.POST.get('pmo')
        seller = request.user.seller_set.filter(pmo=pmo)
        if len(seller) != 1:
            raise Http404
        self.pmo = pmo
        self.seller = seller[0]

