from django.conf.urls import url
from django.views.decorators.csrf import ensure_csrf_cookie

from stall.views import (
    SignupView, ValidateView, LoginView, LogoutView,
    SellerView, ItemView, SubmitView, CancelView,
    PublicApiView
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
    url(r'^api/(?P<method>.+)/$', ensure_csrf_cookie(PublicApiView.as_view()), name='public_api')
]

app_name = 'stall'
