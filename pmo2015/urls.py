from django.conf.urls import include, url
from django.contrib import admin
from pmo2015.views import (
    BaseInfoView, StallView, EventView,
    RegisterView, NewsListView, NewsView,
    QABookView, ApiView
)


urlpatterns = [
    # Examples:
    url(r'^$', 'pmo2015.views.home', name='home'),

    url(r'^baseinfo/$', BaseInfoView.as_view(), name='baseinfo'),
    url(r'^baseinfo/(?P<sub>.+)/$', BaseInfoView.as_view(), name='baseinfo'),

    url(r'^stall/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/$', StallView.as_view(), name='stall'),

    url(r'^event/$', EventView.as_view(), name='event'),
    url(r'^event/(?P<sub>.+)/$', EventView.as_view(), name='event'),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/(?P<sub>.+)/$', RegisterView.as_view(), name='register'),

    url(r'^news/$', NewsListView.as_view(), name='news'),
    url(r'^news/page/(?P<page>\d+)/$', NewsListView.as_view(), name='news'),
    url(r'^news/(?P<news_id>\d+)/$', NewsView.as_view(), name='news'),

    url(r'^qabook/$', QABookView.as_view(), name='qabook'),
    url(r'^qabook/(?P<sub>.+)/$', QABookView.as_view(), name='qabook'),

    url(r'^api/(?P<sub>.+)/$', ApiView.as_view(), name='api'),

    url(r'^test/$', 'pmo2015.views.test', name='test'),
]

