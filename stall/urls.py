from django.conf.urls import include, url
from stall.views import SignupView, ValidateView


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^validate/(?P<validate_code>.+)/$', ValidateView.as_view(), name='validate'),
]
