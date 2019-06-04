from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from stall.forms import LoginForm
from stall.views.bases import ApiView


class LoginView(ApiView):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return self.return_me(1, form.errors)
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(username=email, password=password)
        if user is None:
            return self.return_me(2, "账号与密码不匹配")
        seller = user.seller_set.filter(pmo=form.cleaned_data["pmo"])
        if seller.count() != 1:
            return self.return_me(-2, "不存在该账户")
        seller = seller[0]
        if not seller.is_active:
            return self.return_me(
                3,
                '邮箱未激活，若没有收到邮件请在注册处填写信息重新发送。如有疑问请'
                '<a href="%s" class="maintext-href">联系我们</a>。' %
                reverse("%s:qabook" % form.cleaned_data["pmo"], kwargs={"sub": "guestbook"})
            )
        login(request, user)
        return self.return_me(
            0, "登录成功",
            redirect_to=reverse("dashboard:register", kwargs={"sub": "stall" if seller.is_stall else "consign"})
        )


class LogoutView(ApiView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.return_me(1, "未登录")
        logout(request)
        return self.return_me(0, "注销成功")
