from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .cart import Cart
import os
import json
import stripe


stripe.api_key = settings.STRIPE_HIDDEN


# function to view items in cart
def cart_details(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        x = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total'], product.get_thumbnail, url, product.num_available)

        productsstring = productsstring + x

    # autheticated users details are displayed in the form
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        address = request.user.userprofile.address
        postcode = request.user.userprofile.postcode
        city = request.user.userprofile.city
        phone = request.user.userprofile.phone
    # unautheticated users details are not displayed in the form
    else:
        first_name = last_name = email = address = postcode = city = phone = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'postcode': postcode,
        'city': city,
        'phone': phone,
        'public': settings.STRIPE_API_KEY,
        'productsstring': productsstring.rstrip(',')
    }
    # data is retruned in the cart template page
    return render(request, 'cart.html', context)
