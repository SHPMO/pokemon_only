# coding=utf-8
from django.views.generic import TemplateView


class NewsView(TemplateView):
    template_name = "pmo2015/news.html"
