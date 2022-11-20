import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from .cart import Cart
from apps.store.utilities import StripeWH_Handler, send_order_confirmation, decrement_product_quantity
from apps.order.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
# webhook function for stripe checkout
def webhook(request):
    """Listen for webhooks from Stripe"""
    # # webhook secret key
    wh_secret = settings.STRIPE_WH_SECRET
    # stripe api key to load events from stripe api
    stripe.api_key = settings.STRIPE_HIDDEN

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.headers.get('STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)

    event_dict = event.to_dict()
    if event['type'] == "payment_intent.succeeded":
        payment_intent = event['data']['object']
        order = Order.objects.get(payment_intent=payment_intent.id)
        order.paid = True

        decrement_product_quantity(order)
        send_order_confirmation(order)
        order.save()
        print("Succeeded: ", payment_intent['id'])
        # Fulfill the customer's purchase
    elif event['type'] == "payment_intent.payment_failed":
        payment_intent = event['data']['object']
        error_message = payment_intent['last_payment_error']['message'] if intent.get('last_payment_error') else None
        print("Failed: ", payment_intent['id']), error_message
        # Notify the customer that payment failed
        return HttpResponse(status=500)

    return HttpResponse(status=200)


