# coding=utf-8
from django.views.generic import View
from django.http import Http404, HttpResponse
import json


class ApiView(View):

    def get(self, request, *args, **kwargs):
        raise Http404

    @staticmethod
    def return_me(error_code, message=None, data=None):
        response = {'error': error_code, 'message': message}
        if data is not None and isinstance(data, dict):
            response.update(data)
        return HttpResponse(json.dumps(response), content_type='application/json')
