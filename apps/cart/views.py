from django.shortcuts import render

from .cart import Cart


# function to add item to cart
def cart(request):

    cart_details = Cart(request)

    context = {
        'cart_details': cart_details
    }

    return render(request, 'cart.html', context)
