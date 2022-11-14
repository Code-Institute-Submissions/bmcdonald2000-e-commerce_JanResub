from django.http import JsonResponse

from .models import Coupon


# API for valid coupons
def valid_coupon(request):
    json_response = {}

    coupon_code = request.GET.get('coupon_code', '')

    try:
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            json_response = {'amount': coupon.value}
        else:
            json_response = {'amount': 0}
    except Exception:
        json_response = {'amount': 0}

    return JsonResponse(json_response)
