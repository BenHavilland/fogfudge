from mezzanine.conf import settings
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect

from cartridge.shop.utils import set_shipping
from cartridge.shop.checkout import CheckoutError
def fudge_shipping_handler(request, order_form):
    if is_local(request):
      if request.cart.total_price() >= settings.FREE_SHIP_VALUE:
        set_shipping(request, _("Free Delivery"),0.00)
      else:
        set_shipping(request, _("Pacifica Delivery"),2.00)
    else:
      request.cart.invalid_address = True

def is_local(request):
  if request.POST['shipping_detail_city'].lower() == 'pacifica' \
    and (request.POST['shipping_detail_state'].lower() == 'ca' \
    or request.POST['shipping_detail_state'].lower() == 'california') \
    and request.POST['shipping_detail_postcode'] == '94044':
      return True
  return False

def within_county_limits(request):
  for location in settings.ZIP_CODE_WHITELIST:
    if verify_zip(request, location):
      return True
    if verify_city(request, location):
      return True
  return False

def verify_zip(request, location):
  for zip_code, city in location.items():
    if zip_code == request.POST['shipping_detail_postcode']:
      return True
  return False

def verify_city(request, location):
  for zip_code, city in location.items():
    if city == request.POST['shipping_detail_city']:
      return True
  return False
