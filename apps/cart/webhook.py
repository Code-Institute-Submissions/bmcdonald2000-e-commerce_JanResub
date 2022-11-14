import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .cart import Cart
from apps.store.utilities import decrement_product_quantity, send_order_confirmation
from apps.order.models import Order


@csrf_exempt
# webhook function for stripe checkout
def webhook(request):

    payload = request.body
    event = None

    # stripe api key to load events from stripe api
    stripe.api_key = settings.STRIPE_HIDDEN

    # webhook event loaded from stripe
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )

    # if there is an error then an error message is returned.
    except ValueError as e:
        return HttpResponse(status=400)

    # if payment is successful the order is marked as paid and then saved.
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object

        order = Order.objects.get(payment_intent=payment_intent.id)
        order.paid = True
        order.save()

        # calls function to decrease product quantity after an order is made
        decrement_product_quantity(order)

        # calls fucntion to send order confirmation after an order is made
        send_order_confirmation(self, order)

    return HttpResponse(status=200)
