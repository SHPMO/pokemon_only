# coding=utf-8
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.template import loader

from pmo2015.models import MainComment, BackComment, News, Player
from pmo2015.views.common import CommonView
from stall.models import Seller


class AdminView(CommonView):
    _sub_list = ["news", "backcomment", "battle", "default", 'stall', 'login', 'info']
    name = "admin"
    admin = None

    def _init(self, request):
        if not (request.user.is_authenticated and any(request.user.groups.filter(name='PmoAdminGroup'))):
            raise Http404
        self.admin = request.user.pmoadmin_set.get(pmo='pmo2015')

    def _default(self):
        return redirect("pmo2015:admin")

    def _news_get(self, request, kwargs):
        current = request.GET.get('news_id')
        if current:
            current = News.objects.filter(pk=current)
            if current.count() != 1:
                current = None
            else:
                current = current[0]
        kwargs.update({
            'newslist': News.objects.all(),
            'current': current
        })

    @staticmethod
    def _news_post_return(news_id=None):
        response = redirect("pmo2015:admin", sub='news')
        if news_id:
            response['Location'] += '?news_id=%s' % news_id
        return response

    def _news_post(self, request):
        news_id = request.POST.get('news_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        if request.POST.get('method') == "delete":
            try:
                news = News.objects.get(pk=news_id)
            except News.DoesNotExist:
                raise Http404
            news.delete()
            return self._news_post_return()
        if content == "":
            return self._news_post_return()
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
        return self._news_post_return(news.pk)

    def _backcomment_get(self, request, kwargs):
        current = MainComment.objects.filter(pk=request.GET.get('comment_id'))
        if len(current) != 1:
            current = None
        else:
            current = current[0]
        current_back = request.GET.get('back_id')
        if current and current_back:
            current_back = current.backcomment_set.filter(pk=current_back)
            if current_back.count() != 1:
                current_back = None
            else:
                current_back = current_back[0]
        kwargs.update({
            'main_comments': MainComment.objects.all(),
            'current': current,
            'current_back': current_back
        })

    @staticmethod
    def _backcomment_post_return(comment_id=None):
        response = redirect("pmo2015:admin", sub='backcomment')
        if comment_id:
            response['Location'] += '?comment_id=%s' % comment_id
        return response

    def _backcomment_post(self, request):
        comment_id = int(request.POST.get('comment_id'))
        back_id = request.POST.get('back_id')
        content = request.POST.get('content')
        main_comment = MainComment.objects.filter(pk=comment_id)
        if len(main_comment) != 1:
            raise Http404
        main_comment = main_comment[0]
        method = request.POST.get('method')
        if method == 'delete':
            main_comment.delete()
            return self._backcomment_post_return()
        elif method == 'delete_back':
            back_comment = BackComment.objects.filter(pk=back_id)
            if back_comment.count() == 1:
                back_comment = back_comment[0]
                back_comment.delete()
            return self._backcomment_post_return(main_comment.pk)
        if content == "":
            return self._backcomment_post_return(main_comment.pk)
        if back_id == '-1':
            back_comment = BackComment.create(
                toward=main_comment,
                admin=self.admin,
                content=content,
                ip_address=request.META.get('REMOTE_ADDR')
            )
        else:
            back_comment = BackComment.objects.filter(pk=back_id)
            if back_comment.count() != 1:
                raise Http404
            back_comment = back_comment[0]
            back_comment.content = content
            back_comment.save()
        if main_comment.email and request.POST.get('send_email') == 'send':
            t = MainComment.objects.order_by('-gen_time')
            page = None
            for i in range(t.count()):
                if t[i].pk == comment_id:
                    page = i // 5 + 1
                    break
            if page is None:
                raise Http404
            p = loader.get_template('pmo2015/mails/comment_back.html').render({
                'back_comment': back_comment, 'page': page, 'base_url': settings.BASE_URL
            })
            send_mail(
                '%s留言回复' % settings.EMAIL_SUBJECT_PREFIX, "",
                settings.EMAIL_HOST_USER, [main_comment.email], fail_silently=False,
                html_message=p
            )
        return self._backcomment_post_return(main_comment.pk)

    def _battle_get(self, request, kwargs):
        current = Player.objects.filter(pk=request.GET.get('player_id'))
        if current.count() == 1:
            current = current[0]
        else:
            current = None
        player_list = Player.objects.all()
        kwargs.update({
            'current': current,
            'player_list': player_list
        })

    def _battle_post(self, request):
        me = request.POST.get('submit')
        current = Player.objects.filter(pk=request.POST.get('player_id'))
        if current.count() != 1:
            raise Http404
        current = current[0]
        if me == 'accept':
            current.do_validate(True)
        elif me == 'reject':
            current.do_validate(False)
        else:
            raise Http404
        send_mail(
            '%s对战报名结果' % settings.EMAIL_SUBJECT_PREFIX, "",
            settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
            html_message=loader.get_template('pmo2015/mails/battle_validated.html').render({
                'player': current, 'base_url': settings.BASE_URL,
                'message': request.POST.get('message'), 'signup_id': '%03d' % current.pk
            })
        )
        response = redirect("pmo2015:admin", sub='battle')
        response['Location'] += '?player_id=%s' % current.pk
        return response

    def _info_get(self, request, kwargs):
        kwargs.update({
            'admin': self.admin
        })

    def _info_post(self, request):
        pwd = request.POST.get('password')
        ncn = request.POST.get('nickname')
        if pwd:
            self.admin.user.set_password(pwd)
            self.admin.user.save()
        if ncn:
            self.admin.nickname = ncn
            self.admin.save()
        return redirect("pmo2015:admin", sub='info')

    def _stall_get(self, request, kwargs):
        current = Seller.objects.filter(pmo=self.pmo, pk=request.GET.get('seller_id'))
        if current.count() == 1:
            current = current[0]
        else:
            current = None
        kwargs.update({
            'current': current,
            'sellers': Seller.objects.filter(pmo=self.pmo)
        })

    def _stall_post(self, request):
        me = request.POST.get('submit')
        current = Seller.objects.filter(pmo=self.pmo, pk=request.POST.get('seller_id'))
        if current.count() != 1:
            raise Http404
        current = current[0]
        if me == 'notice':
            notice = request.POST.get('notice')
            if notice:
                current.notice = notice
                current.save()
                if request.POST.get('send_email') == 'send':
                    send_mail(
                        '%s%s通知' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
                        settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
                        html_message=loader.get_template('pmo2015/mails/seller_notice.html').render({
                            'seller': current, 'base_url': settings.BASE_URL,
                        })
                    )
            response = redirect("pmo2015:admin", sub='stall')
            response['Location'] += '?seller_id=%s' % current.pk
            return response
        elif me == 'accept':
            current.do_validate(True)
        elif me == 'reject':
            current.do_validate(False)
        elif me == 'setid':
            seller_id = request.POST.get('sellerid')
            if seller_id:
                current.seller_id = seller_id
                current.save()
                if request.POST.get('send_email') == 'send':
                    send_mail(
                        '%s%s通知' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
                        settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
                        html_message=loader.get_template('pmo2015/mails/seller_sellerid.html').render({
                            'seller': current, 'base_url': settings.BASE_URL,
                        })
                    )
            response = redirect("pmo2015:admin", sub='stall')
            response['Location'] += '?seller_id=%s' % current.pk
            return response
        else:
            raise Http404
        send_mail(
            '%s%s申请结果' % (settings.EMAIL_SUBJECT_PREFIX, "摊位" if current.is_stall else "寄卖"), "",
            settings.EMAIL_HOST_USER, [current.email], fail_silently=False,
            html_message=loader.get_template('pmo2015/mails/seller_validated.html').render({
                'seller': current, 'base_url': settings.BASE_URL,
                'message': request.POST.get('message', '')
            })
        )
        response = redirect("pmo2015:admin", sub='stall')
        response['Location'] += '?seller_id=%s' % current.pk
        return response

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
            self._news_get(request, kwargs)
        elif sub == 'backcomment':
            self._backcomment_get(request, kwargs)
        elif sub == 'battle':
            self._battle_get(request, kwargs)
        elif sub == 'info':
            self._info_get(request, kwargs)
        elif sub == 'stall':
            self._stall_get(request, kwargs)
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None):
        if sub == 'login':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is None or not any(user.groups.filter(name='PmoAdminGroup')):
                response = redirect("pmo2015:admin", sub='login')
                response['Location'] += '?fail=1'
                return response
            login(request, user)
            return self._default()
        self._init(request)
        if sub == 'news':
            return self._news_post(request)
        elif sub == 'backcomment':
            return self._backcomment_post(request)
        elif sub == 'battle':
            return self._battle_post(request)
        elif sub == 'info':
            return self._info_post(request)
        elif sub == 'stall':
            return self._stall_post(request)
        else:
            raise Http404
