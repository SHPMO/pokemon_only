from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'msite.views.home', name='home'),
    url(r'^pmo2015/', include('pmo2015.urls', namespace='pmo2015', app_name='pmo2015')),
    url(r'^pmo2016/', include('pmo2016.urls', namespace='pmo2016', app_name='pmo2016')),
    url(r'^pmo2017/', include('pmo2017.urls', namespace='pmo2017', app_name='pmo2017')),
    url(r'^stall/', include('stall.urls', namespace='stall', app_name='stall')),

    url(r'^django_admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
