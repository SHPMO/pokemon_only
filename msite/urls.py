from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import msite.views

urlpatterns = [
    url(r'^$', msite.views.home, name='home'),
    url(r'^pmo2015/', include('pmo2015.urls', namespace='pmo2015')),
    url(r'^pmo2016/', include('pmo2016.urls', namespace='pmo2016')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^stall/', include('stall.urls', namespace='stall')),
    url(r'^django_admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
