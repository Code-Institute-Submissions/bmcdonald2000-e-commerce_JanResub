import json
import stripe
from .models import Product
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from apps.order.views import render_to_pdf
from django. conf import settings

from apps.cart.cart import Cart
from apps.order.utils import checkout
from apps.order.models import Order
from apps.coupon.models import Coupon
from .utilities import decrement_product_quantity, send_order_confirmation


# api function to create a checkout session
def checkout_session(request):

    data = json.loads(request.body)

    coupon_code = data['coupon_code']
    coupon_value = 0

    # Coupon code
    if coupon_code != '':
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            coupon_value = coupon.value
            coupon.use()

    cart = Cart(request)
    # retrives hidden stripe variable
    stripe.api_key = settings.STRIPE_HIDDEN

    items = []
    # calculates the price before and after a coupon is applied.
    for item in cart:
        product = item['product']

        price = int(product.price * 100)

        if coupon_value > 0:
            price = int(price - (price * (int(coupon_value) / 100)))

        obj = {
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': product.title
                },
                'unit_amount': price
            },
            'quantity': item['quantity']
        }

        items.append(obj)

    # creates a session for the stripe checkout
    session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='https://tranquil-temple-81228.herokuapp.com/cart/success/',
            cancel_url='https://tranquil-temple-81228.herokuapp.com/cart/cancel'
    )

    # creates an order
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    postcode = data['postcode']
    city = data['city']
    phone = data['phone']
    payment_intent = session.payment_intent

    orderid = checkout(request, data['first_name'], data['last_name'], data['email'], data['address'], data['postcode'], data['city'], data['phone'])

    total = 0.00

    # when an Item is in the cart the data is saved until the session expires

    for item in cart:
        product = item['product']
        total = total + (float(product.price) * int(item['quantity']))

    if coupon_value > 0:
        price = price * (coupon_value / 100)

    order = Order.objects.get(pk=orderid)
    order.payment_intent = payment_intent
    order.amount_paid = total
    order.used_coupon = coupon_code
    order.paid = True
    order.save()

    for item in order.items.all():
        product = item.product
        product.num_available = product.num_available - item.quantity
        product.save()

    return JsonResponse({'session': session})


# checkout api function
def Checkout(request):
    cart = Cart(request)

    data = json.loads(request.body)
    jsonresponse = {'success': True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    postcode = data['postcode']
    city = data['city']

    orderid = checkout(request, first_name, last_name, email, address, postcode, city)

    paid = True

    if paid == True:
        order = Order.objects.get(pk=orderid)
        order.paid = True
        order.amount_paid = cart.total_cost()
        order.save()

        decrement_product_quantity(order)
        send_order_confirmation(order)

        cart.clear()

    return JsonResponse(jsonresponse)


#  add items api function
def add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)


# delete items api function
def delete_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']

    cart = Cart(request)
    cart.delete(product_id)

    return JsonResponse(jsonresponse)
