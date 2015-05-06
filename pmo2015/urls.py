from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'pmo2015.views.home', name='home'),
    url(r'^test/$', 'pmo2015.views.test', name='test'),
]
