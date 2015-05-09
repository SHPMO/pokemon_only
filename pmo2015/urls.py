from django.conf.urls import include, url
from django.contrib import admin
from pmo2015.views import BaseInfoView

urlpatterns = [
    # Examples:
    url(r'^$', 'pmo2015.views.home', name='home'),

    url(r'^baseinfo/$', BaseInfoView.as_view(), name='baseinfo'),
    url(r'^baseinfo/(?P<sub>.+)/$', BaseInfoView.as_view(), name='baseinfo'),

    url(r'^stall/$', BaseInfoView.as_view(), name='stall'),
    url(r'^event/$', BaseInfoView.as_view(), name='event'),
    url(r'^register/$', BaseInfoView.as_view(), name='register'),
    url(r'^news/$', BaseInfoView.as_view(), name='news'),
    url(r'^qabook/$', BaseInfoView.as_view(), name='qabook'),


    url(r'^test/$', 'pmo2015.views.test', name='test'),
]
