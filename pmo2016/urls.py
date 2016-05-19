from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'pmo2016.views.home', name='home'),
]

