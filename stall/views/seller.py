from django.http import Http404
from stall.views.bases import AuthedApiView
from stall.forms import SellerForm


class SellerView(AuthedApiView):
    def post(self, request, sub=None, *args, **kwargs):
        super().post(request, *args, **kwargs)
        if sub == 'upload':
            image = request.FILES['circle_image']
            if image:
                if image.size > (1 << 20):
                    return self.return_me(1, '请上传小于 1 MB 的图片')
                try:
                    self.seller.circle_image = image
                except:
                    return self.return_me(2, '未知错误')
            self.seller.save()
            return self.return_me(0, '上传成功', circle_image_url=self.seller.circle_image.url)
        form = SellerForm(request.POST, request.FILES)
        if not form.is_valid():
            return self.return_me(1, '*为必填项')
        if self.seller.is_stall and len(form.cleaned_data['proposer_id']) != 18:
            return self.return_me(2, '身份证号码错误')
        self.seller.circle_name = form.cleaned_data['circle_name']
        self.seller.circle_description = form.cleaned_data['circle_description']
        self.seller.proposer_name = form.cleaned_data['proposer_name']
        self.seller.proposer_sex = form.cleaned_data['proposer_sex']
        self.seller.proposer_qq = form.cleaned_data['proposer_qq']
        self.seller.proposer_phone = form.cleaned_data['proposer_phone']
        self.seller.proposer_id = form.cleaned_data['proposer_id']
        self.seller.save()
        return self.return_me(0, '保存成功')
