from django.conf.urls import url
from stall.views import SignupView, ValidateView, LoginView, SellerView


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^validate/$', ValidateView.as_view(), name='validate'),
    url(r'^seller/$', SellerView.as_view(), name='seller'),
    url(r'^seller/(?P<sub>.+)/$', SellerView.as_view(), name='seller'),
]
