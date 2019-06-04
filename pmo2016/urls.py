from django.conf.urls import url

import pmo2016.views.home
from pmo2016.views import (
    BaseInfoView, StallView, EventView,
    RegisterView,
    QABookView, ApiView, AdminView
)

urlpatterns = [
    url(r'^$', pmo2016.views.home, name='home'),

    url(r'^baseinfo/$', BaseInfoView.as_view(), name='baseinfo'),
    url(r'^baseinfo/(?P<sub>.+)/$', BaseInfoView.as_view(), name='baseinfo'),

    url(r'^stall/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/(?P<subsub>\d+)/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/$', StallView.as_view(), name='stall'),

    url(r'^event/$', EventView.as_view(), name='event'),
    url(r'^event/(?P<sub>.+)/$', EventView.as_view(), name='event'),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/(?P<sub>.+)/$', RegisterView.as_view(), name='register'),

    url(r'^qabook/$', QABookView.as_view(), name='qabook'),
    url(r'^qabook/(?P<sub>.+)/$', QABookView.as_view(), name='qabook'),

    url(r'^api/(?P<sub>.+)/$', ApiView.as_view(), name='api'),

    url(r'^admin/$', AdminView.as_view(), name='admin'),
    url(r'^admin/(?P<sub>.+)/$', AdminView.as_view(), name='admin'),

    # url(r'^test/$', 'pmo2016.views.test', name='test'),
]

app_name = 'pmo2016'
