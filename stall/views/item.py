from django.http import Http404
from stall.views.bases import AuthedApiView
from stall.forms import SellerForm


class ItemView(AuthedApiView):
    def post(self, request, sub=None, *args, **kwargs):
        super().post(request, *args, **kwargs)
        seller = request.user.seller
        if sub == 'upload':
            image = request.FILES['circle_image']
            if image:
                if image.size > (1 << 20):
                    return self.return_me(1, '文件过大')
                try:
                    seller.circle_image = image
                except:
                    self.return_me(2, '未知错误')
            seller.save()
            return self.return_me(0, '上传成功', circle_image_url=seller.circle_image.url)
        form = SellerForm(request.POST, request.FILES)
        if not form.is_valid():
            return self.return_me(1, '*为必填项')
        if seller.is_stall and len(form.cleaned_data['proposer_id']) != 18:
            return self.return_me(2, '身份证号码错误')
        seller.circle_name = form.cleaned_data['circle_name']
        seller.circle_description = form.cleaned_data['circle_description']
        seller.proposer_name = form.cleaned_data['proposer_name']
        seller.proposer_sex = form.cleaned_data['proposer_sex']
        seller.proposer_qq = form.cleaned_data['proposer_qq']
        seller.proposer_phone = form.cleaned_data['proposer_phone']
        seller.proposer_id = form.cleaned_data['proposer_id']
        seller.save()
        return self.return_me(0, '保存成功')
