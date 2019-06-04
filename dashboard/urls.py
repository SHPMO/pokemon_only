from django.conf.urls import url

from dashboard.views import (
    StallView,
    RegisterView,
    AdminView
)

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/(?P<sub>.+)/$', RegisterView.as_view(), name='register'),

    url(r'^stall/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/(?P<subsub>\d+)/$', StallView.as_view(), name='stall'),
    url(r'^stall/(?P<sub>.+)/$', StallView.as_view(), name='stall'),

    url(r'^admin/$', AdminView.as_view(), name='admin'),
    url(r'^admin/(?P<sub>.+)/$', AdminView.as_view(), name='admin'),

    # url(r'^test/$', 'dashboard.views.test', name='test'),
]

app_name = 'dashboard'
