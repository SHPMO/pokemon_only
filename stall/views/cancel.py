from stall.views.bases import AuthedApiView
from stall.forms import SubmitForm


class CancelView(AuthedApiView):
    def post(self, request, sub=None, *args, **kwargs):
        x = super().post(request, False, *args, **kwargs)
        if x:
            return x
        try:
            self.seller.status = 1
            self.seller.save()
        except:
            return self.return_me()
        return self.return_me(0, '撤销成功')
