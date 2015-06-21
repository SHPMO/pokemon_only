from django.http import Http404
from pmo2015.views.common import CommonView
from stall.models import Seller, Item


class StallView(CommonView):
    _sub_list = ["diagram", "circle", "items", "item", "circles"]
    name = "stall"
    has_perm = False

    def _circle_get(self, kwargs):
        if self.has_perm:
            sellers = Seller.objects.filter(pmo=self.pmo)
        else:
            sellers = Seller.objects.filter(pmo=self.pmo, status=3)
        stalls = sellers.filter(is_stall=True)
        consigns = sellers.filter(is_stall=False)
        kwargs.update({
            'stalls': stalls,
            'consigns': consigns
        })

    def _circle_detail_get(self, circle_id, page, kwargs):
        seller = Seller.objects.filter(pmo=self.pmo, pk=circle_id)
        if seller.count() != 1:
            raise Http404
        seller = seller[0]
        if not self.has_perm and seller.status != 3:
            raise Http404
        total = (seller.item_set.count() + 4) // 5
        items = seller.item_set.all()[page * 5 - 5:page * 5]
        kwargs.update({
            'seller': seller,
            'items': items,
            'prev': page - 1 if page > 1 else None,
            'next': page + 1 if page < total else None
        })

    def _item_get(self, page, kwargs):
        if self.has_perm:
            items = Item.objects.filter(pmo=self.pmo)
        else:
            items = Item.objects.filter(pmo=self.pmo, validated=True)
        total = (items.count() + 9) // 10
        items = items[page * 10 - 10:page * 10]
        if items.count() == 0:
            itemlist = None
        else:
            itemlist = [(items[0].seller, [items[0]])]
            for i in range(1, len(items)):
                if items[i].seller == items[i-1].seller:
                    itemlist[-1][1].append(items[i])
                else:
                    itemlist.append((items[i].seller, [items[i]]))
        kwargs.update({
            'itemlist': itemlist,
            'prev': page - 1 if page > 1 else None,
            'next': page + 1 if page < total else None
        })

    def _item_detail_get(self, item_id, kwargs):
        item = Item.objects.filter(pmo=self.pmo, pk=item_id)
        if item.count() != 1:
            item = None
        else:
            item = item[0]
            if not (self.has_perm or item.validated):
                item = None
        kwargs.update({
            'item': item
        })

    def get(self, request, sub=None, subsub=None, *args, **kwargs):
        print(sub)
        print(subsub)
        if sub in {'circles', 'items'}:
            raise Http404
        if request.user.is_authenticated() and any(request.user.groups.filter(name='Pmo2015AdminGroup')):
            self.has_perm = True
        if sub == 'circle':
            if subsub is None:
                sub = 'circles'
                self._circle_get(kwargs)
            else:
                page = int(request.GET.get('page', 1))
                self._circle_detail_get(subsub, page, kwargs)
        elif sub == 'item':
            if subsub is None:
                sub = 'items'
                page = int(request.GET.get('page', 1))
                self._item_get(page, kwargs)
            else:
                self._item_detail_get(subsub, kwargs)

        return super().get(request, sub, *args, **kwargs)
