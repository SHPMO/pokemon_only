# coding=utf-8
from django.views.generic import TemplateView
from django.http import Http404
from pmo2015.models import News


class NewsListView(TemplateView):
    template_name = "pmo2015/news/newslist.html"

    def get(self, request, page=None, *args, **kwargs):
        if page is None:
            page = 1
        kwargs.update({
            'newslist': News.objects.order_by('-gen_time')[page * 5 - 5:page * 5]
        })
        return super().get(request, *args, **kwargs)


class NewsView(TemplateView):
    template_name = "pmo2015/news/news.html"

    def get(self, request, news_id=None, *args, **kwargs):
        if news_id is None:
            raise Http404
        try:
            news = News.objects.get(pk=news_id)
        except News.DoesNotExist:
            news = None
        kwargs.update({
            'news': news
        })
        return super().get(request, *args, **kwargs)
