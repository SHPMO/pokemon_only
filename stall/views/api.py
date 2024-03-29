from django.http import Http404

from stall.models import Item, Seller
from stall.views.bases import ApiView


class PublicApiView(ApiView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method_dict = {
            "test": self._test,
            "get_item": self._get_item,
            "get_seller": self._get_seller,
        }

    def get(self, request, method=None, *args, **kwargs):
        if method not in self.method_dict:
            return self.return_me(4, "未知方法")
        self.pmo = request.GET.get("pmo")
        if not self.pmo:
            return self.return_me(5, "未知PMO")
        return self.method_dict[method](request, *args, **kwargs)

    def post(self, request, method, *args, **kwargs):
        raise Http404

    @staticmethod
    def _item_info(item):
        return dict(
            item_id=item.pk, seller_id=item.seller_id,
            name=item.name, item_type=item.item_type,
            content=item.content, price=item.price,
            url=item.url, authors=item.authors,
            introduction=item.introduction, forto=item.forto,
            cover_image=item.cover_image.url if item.cover_image else None,
            is_restricted=item.is_restricted, circle=item.circle,
            is_started_with=item.is_started_with, item_pictures=[
                picture.picture.url for picture in item.itempicture_set.all() if picture.picture
            ], item_order=item.item_order
        )

    def _test(self, request, *args, **kwargs):
        return self.return_me(0, "success")

    def _get_item(self, request, *args, **kwargs):
        item_id = request.GET.get("item_id")
        if item_id:
            items = Item.objects.filter(
                pk=item_id,
                validated=True,
                pmo=self.pmo
            )
            return self.return_me(
                0, "OK", data=self._item_info(items[0])
            ) if items.count() == 1 else self.return_me(-1, "找不到商品")
        seller_id = request.GET.get("seller_id")
        if seller_id:
            items = Item.objects.filter(
                seller_id=seller_id,
                validated=True,
                pmo=self.pmo
            )
            return self.return_me(
                0, "OK", data={
                    item.pk: self._item_info(item) for item in items
                }
            ) if items.count() > 0 else self.return_me(-1, "找不到商家")
        items = Item.objects.filter(
            validated=True,
            pmo=self.pmo
        )
        return self.return_me(0, "OK", data={
            item.pk: self._item_info(item) for item in items
        })

    @staticmethod
    def _seller_info(seller):
        return dict(
            id=seller.pk, circle_name=seller.circle_name,
            circle_description=seller.circle_description,
            circle_image=seller.circle_image.url if seller.circle_image else None,
            seller_id=seller.seller_id, items=[
                item.pk for item in seller.item_set.filter(validated=True)
            ]
        )

    def _get_seller(self, request, *args, **kwargs):
        seller_id = request.GET.get("seller_id")
        if seller_id:
            sellers = Seller.objects.filter(
                pk=seller_id,
                status=3,
                is_active=True,
                pmo=self.pmo
            )
            return self.return_me(
                0, "OK", data=self._seller_info(sellers[0])
            ) if sellers.count() == 1 else self.return_me(-1, "找不到商家")
        sellers = Seller.objects.filter(
            is_active=True,
            status=3,
            pmo=self.pmo
        )
        return self.return_me(0, "OK", data={
            seller.pk: self._seller_info(seller) for seller in sellers
        })
