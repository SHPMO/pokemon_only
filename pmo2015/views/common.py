# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CommonView(TemplateView):
    _sub_list = {}
    name = ''

    def get(self, request, sub=None, *args, **kwargs):
        if not sub:
            return redirect(reverse("pmo2015:%s" % self.name, args=[self._sub_list[0]]))
        if sub in self._sub_list:
            self.template_name = "pmo2015/%s/%s.html" % (self.name, sub)
            return super().get(request, *args, **kwargs)
        raise Http404


class BaseInfoView(CommonView):
    _sub_list = ["schedule", "place", "ticket", "prize"]
    name = "baseinfo"


class StallView(CommonView):
    _sub_list = ["diagram", "circle", "goods"]
    name = "stall"


class EventView(CommonView):
    _sub_list = ["battle", "stage", "venue", "raffle"]
    name = "event"
