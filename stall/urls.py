from django.conf.urls import url
from stall.views import (
    SignupView, ValidateView, LoginView, LogoutView,
    SellerView, ItemView, SubmitView, CancelView
)

urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^validate/$', ValidateView.as_view(), name='validate'),
    url(r'^seller/$', SellerView.as_view(), name='seller'),
    url(r'^seller/(?P<sub>.+)/$', SellerView.as_view(), name='seller'),
    url(r'^item/$', ItemView.as_view(), name='item'),
    url(r'^submit/$', SubmitView.as_view(), name='submit'),
    url(r'^cancel/$', CancelView.as_view(), name='cancel'),
]
