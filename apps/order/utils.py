import datetime
import os

from random import randint

from apps.cart.cart import Cart
from apps.order.models import Order, Item


def checkout(request, first_name, last_name, email, address, postcode, city, phone):
    order = Order(first_name=first_name, last_name=last_name, email=email, address=address, postcode=postcode, city=city, phone=phone)

    if request.user.is_authenticated:
        order.user = request.user

    order.save()

    cart = Cart(request)

    for item in cart:
        Item.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    return order.id
