from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'msite.views.home', name='home'),
    url(r'^pmo2015/', include('pmo2015.urls', namespace='pmo2015', app_name='pmo2015')),
    url(r'^django_admin/', include(admin.site.urls)),
]
