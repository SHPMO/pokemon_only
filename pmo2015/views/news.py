# coding=utf-8
from django.views.generic import TemplateView
from django.http import Http404


class NewsListView(TemplateView):
    template_name = "pmo2015/news/newslist.html"

    def get(self, request, page=None, *args, **kwargs):
        if page is None:
            page = 1
        return super().get(request, *args, **kwargs)


class NewsView(TemplateView):
    template_name = "pmo2015/news/news.html"

    def get(self, request, news_id=None, *args, **kwargs):
        if news_id is None:
            raise Http404
        return super().get(request, *args, **kwargs)
