import os
from django.template.loader import render_to_string
from apps.order.views import render_to_pdf
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from apps.order.models import Order, Item

import json
import time

@csrf_exempt

# fucntion to decrease product quantity after it has been purchased
def decrement_product_quantity(order):
    for item in order.items.all():
        product = item.product
        product.num_available = product.num_available - item.quantity
        product.save()

# fucntion to send order confirmation
def send_order_confirmation(order):
    """Send the user a confirmation email"""
    recipient_list = [order.email]
    subject = render_to_string(
        'confirmation_email/subject.txt',
        {'order': order})
    body = render_to_string(
        'confirmation_email/body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    message = send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        )
    
    pdf = render_to_pdf('order_pdf.html', {'order': order})

    if pdf:
        name = 'order_%s.pdf' % order.id
        message.attach(name, pdf, 'application/pdf')

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


