from django.core import serializers
from django.http import Http404
import json
from stall.views.bases import AuthedApiView
from stall.forms import ItemForm
from stall.models import Item, ItemPicture


class ItemView(AuthedApiView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method_dict = {
            "add_item": self._add_item,
            "delete_item": self._delete_item,
            "upload_image": self._upload_image,
            "delete_image": self._delete_image,
            "save": self._save
        }

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        method = request.POST.get('method')
        if method not in self.method_dict:
            return self.return_me(4, '未知方法')
        return self.method_dict[method](request, *args, **kwargs)

    def _required_item(self, request):
        item = Item.objects.filter(
            pk=request.POST.get('item_id'),
            seller=self.seller,
            pmo=self.pmo
        )
        if len(item) == 1:
            return item[0]
        return None

    def _upload_image(self, request, *args, **kwargs):
        item = self._required_item(request)
        if item is None:
            return self.return_me(3, '未指定物品')

        image = request.FILES.get('cover_image')
        if image:
            try:
                item.cover_image = image
                item.save()
            except:
                return self.return_me(-1, '未知错误')
            return self.return_me(
                0, "上传成功",
                image_url=item.url,
                image_id=0
            )
        for akey in request.FILES:
            if akey.startswith('item_image_'):
                image = request.FILES[akey]
                break
        if not image:
            return self.return_me(2, '无数据')
        if image.size > (1 << 20):
            return self.return_me(1, '请上传小于 1 MB 的图片')
        try:
            item_picture = ItemPicture.create(
                item,
                request.POST['pmo'],
                picture=image
            )
        except:
            return self.return_me(-1, '未知错误')
        return self.return_me(
            0, '上传成功',
            image_url=item_picture.picture.url,
            image_id=item_picture.pk
        )

    def _delete_image(self, request, *args, **kwargs):
        item = self._required_item(request)
        if item is None:
            return self.return_me(3, '未指定物品')
        image_id = request.POST.get('imgae_id')
        if image_id == '0':
            try:
                item.cover_image = None
                item.save()
            except:
                return self.return_me(-1, "未知错误")
            return self.return_me(0, '删除成功')
        try:
            item_picture = ItemPicture.objects.filter(
                pk=image_id,
                item=item,
                pmo=self.pmo
            )
            if len(item_picture) != 1:
                return self.return_me(5, '不存在的id')
            item_picture.delete()
        except:
            return self.return_me(-1, "未知错误")
        return self.return_me(0, '删除成功')

    def _add_item(self, request):
        item = Item.create(self.seller, request.POST.get('pmo'))
        if item is None:
            return self.return_me(3, '未指定物品')
        return self.return_me(0, "添加成功", item_id=item.pk)

    def _delete_item(self, request, *args, **kwargs):
        pass

    def _save(self, request, *args, **kwargs):
        ItemForm(request.POST)
        pass
