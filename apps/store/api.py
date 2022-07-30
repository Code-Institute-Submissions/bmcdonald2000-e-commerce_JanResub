import json
from .models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from apps.cart.cart import Cart
from apps.order.utils import checkout
from apps.order.models import Order, Item


# checkout api function
def Checkout(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    postcode = data['postcode']
    city = data['city']

    cart = Cart(request)

    orderid = checkout(request, first_name, last_name, email, address, postcode, city)

    paid = True

    if paid == True:
        order = Order.objects.get(pk=orderid)
        order.paid = True
        order.amount_paid = cart.total_cost()
        order.save()

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
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.delete(product_id)

    return JsonResponse(jsonresponse)
