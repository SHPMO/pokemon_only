from pmo2015.views.common import CommonView
from stall.models import Seller


class StallView(CommonView):
    _sub_list = ["diagram", "circle", "items"]
    name = "stall"

    def get(self, request, sub=None, *args, **kwargs):
        if request.user.is_authenticated() and any(request.user.groups.filter(name='Pmo2015AdminGroup')):
            has_perm = True
        else:
            has_perm = False
        if sub == 'circle':
            if has_perm:
                stalls = Seller.objects.filter(pmo='pmo2015', is_stall=True)
            else:
                stalls = Seller.objects.filter(pmo='pmo2015', is_stall=True, status=3)
            kwargs.update({
                'stalls': stalls,
                'has_perm': has_perm
            })
        return super().get(request, sub, *args, **kwargs)
