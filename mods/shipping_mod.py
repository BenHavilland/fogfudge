from mezzanine.conf import settings
from django.utils.translation import ugettext as _

from cartridge.shop.utils import set_shipping

def fudge_shipping_handler(request, order_form):

    # Check for the locals
    isLocal = False
    if request.POST['shipping_detail_city'].lower() == 'pacifica' \
      and (request.POST['shipping_detail_state'].lower() == 'ca' \
      or request.POST['shipping_detail_state'].lower() == 'california') :
        isLocal = True
    elif request.POST['shipping_detail_postcode'] == '94044':
        isLocal = True
    if isLocal:
      set_shipping(request, _("Free shipping for locals"),0.00)
      return()

    # Check for free shipping theshold
    if request.cart.total_price() >= settings.FREE_SHIP_VALUE:
      set_shipping(request, _("Free shipping"),0.00)
      return()
    else:
      spendMore = settings.FREE_SHIP_VALUE - request.cart.total_price()
    if not request.session.get("free_shipping"):
        settings.use_editable()
        set_shipping(request, _("Spend only $"+str(spendMore)+" more and get free shipping. Shipping"),
                     settings.SHOP_DEFAULT_SHIPPING_VALUE)
