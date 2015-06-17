from django.http import Http404
from pmo2015.views.common import CommonView
from stall.models import Seller


class StallView(CommonView):
    _sub_list = ["diagram", "circle", "items", "detail"]
    name = "stall"

    def _circle_get(self, has_perm, kwargs):
        if has_perm:
            sellers = Seller.objects.filter(pmo=self.pmo)
        else:
            sellers = Seller.objects.filter(pmo=self.pmo, status=3)
        stalls = sellers.filter(is_stall=True)
        consigns = sellers.filter(is_stall=False)
        kwargs.update({
            'stalls': stalls,
            'consigns': consigns
        })

    def _circle_detail_get(self, tp, pa, has_perm, kwargs):
        if tp == 'stall':
            is_stall = True
        elif tp == 'consign':
            is_stall = False
        else:
            raise Http404
        seller = Seller.objects.filter(pmo=self.pmo, is_stall=is_stall, pk=pa)
        if len(seller) != 1:
            raise Http404
        seller = seller[0]
        if not has_perm and seller.status != 3:
            raise Http404
        kwargs.update({
            'seller': seller
        })

    def get(self, request, sub=None, subsub=None, *args, **kwargs):
        if sub in {'detail'}:
            raise Http404
        if request.user.is_authenticated() and any(request.user.groups.filter(name='Pmo2015AdminGroup')):
            has_perm = True
        else:
            has_perm = False
        if sub == 'circle':
            tp = request.GET.get('type')
            pa = request.GET.get('p')
            if all((tp, pa)):
                sub = 'detail'
                self._circle_detail_get(tp, pa, has_perm, kwargs)
            else:
                self._circle_get(has_perm, kwargs)

        return super().get(request, sub, *args, **kwargs)
