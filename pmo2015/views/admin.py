# coding=utf-8
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from pmo2015.models import MainComment, BackComment, PmoAdmin, News
from pmo2015.views.common import CommonView


class AdminView(CommonView):
    _sub_list = ["news", "backcomment", "battle", "default", 'stall', 'login']
    name = "admin"
    admin = None

    def _init(self, request):
        if not (request.user.is_authenticated() and any(request.user.groups.filter(name='PMOAdminGroup'))):
            raise Http404
        self.admin = request.user.pmoadmin

    def _default(self):
        return redirect("pmo2015:admin")

    def get(self, request, sub=None, *args, **kwargs):
        if sub == 'login':
            if request.GET.get('fail') == '1':
                kwargs['fail'] = True
            return super().get(request, sub, *args, **kwargs)
        self._init(request)
        if sub == 'logout':
            logout(request)
            return self._default()
        if sub == 'default':
            raise Http404
        if sub is None:
            sub = 'default'
        kwargs.update({
            'admin': self.admin
        })
        if sub == 'news':
            current = request.GET.get('news_id')
            if current:
                current = News.objects.filter(pk=current)
                if len(current) != 1:
                    current = None
                else:
                    current = current[0]
            kwargs.update({
                'newslist': News.objects.all(),
                'current': current
            })
        elif sub == 'backcomment':
            pass
        self.template_name = sub
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None):
        if sub == 'login':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is None or not any(user.groups.filter(name='PMOAdminGroup')):
                response = redirect("pmo2015:admin", sub='login')
                response['Location'] += '?fail=1'
                return response
            login(request, user)
            return self._default()
        self._init(request)
        if sub == 'news':
            news_id = request.POST.get('news_id')
            title = request.POST.get('title')
            content = request.POST.get('content')
            if news_id == '-1':
                news = News.create(
                    title=title,
                    content=content,
                    user=self.admin,
                    ip_address=request.META.get('REMOTE_ADDR')
                )
            else:
                try:
                    news = News.objects.get(pk=news_id)
                except News.DoesNotExist:
                    raise Http404
                news.title = title
                news.content = content
                news.save()
            response = redirect("pmo2015:admin", sub='news')
            response['Location'] += '?news_id=%s' % news.pk
            return response
        else:
            raise Http404
