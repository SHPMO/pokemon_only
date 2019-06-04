from stall.forms import SubmitForm
from stall.views.bases import AuthedApiView


class SubmitView(AuthedApiView):
    def post(self, request, sub=None, *args, **kwargs):
        x = super().post(request, *args, **kwargs)
        if x:
            return x
        form = SubmitForm(request.POST, request.FILES)
        if not form.is_valid():
            return self.return_me(1, '请勾选复选框')

        if self.seller.is_stall:
            try:
                self.seller.booth = form.cleaned_data['booth']
            except KeyError:
                return self.return_me(2, '请输入摊位数')
        self.seller.number_of_people = form.cleaned_data['number_of_people']
        try:
            self.seller.remarks = form.cleaned_data['remarks']
            self.seller.status = 2
            self.seller.save()
        except:
            return self.return_me()
        return self.return_me(0, '保存成功')
