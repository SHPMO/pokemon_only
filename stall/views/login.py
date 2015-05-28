# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from stall.views.bases import ApiView, View
from stall.forms import LoginForm


class LoginView(ApiView):

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return self.return_me(1, form.errors)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return self.return_me(2, "账号与密码不匹配")
        seller = user.seller
        if not seller.is_active:
            return self.return_me(
                3,
                '邮箱未激活，若没有收到邮件请在注册处填写信息重新发送。如有疑问请<a href="%s">联系我们</a>。' %
                reverse("%s:qabook" % seller.pmo, {"sub": "guestbook"})
            )
        return self.return_me(0, "登录成功")
