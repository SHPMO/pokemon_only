# coding=utf-8
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CommonView(TemplateView):
    _sub_list = []
    name = ''
    pmo = settings.CURRENT_PMO

    def get(self, request, sub=None, *args, **kwargs):
        if not sub:
            return redirect("dashboard:%s" % self.name, sub=self._sub_list[0])
        if sub in self._sub_list:
            self.template_name = "dashboard/%s/%s.html" % (self.name, sub)
            return super().get(request, *args, **kwargs, pmo=self.pmo)
        raise Http404
