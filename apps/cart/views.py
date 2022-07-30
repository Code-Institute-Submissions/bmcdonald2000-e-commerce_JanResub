from django.shortcuts import render

from .cart import Cart


# function to add item to cart
def cart(request):
    cart_details = Cart(request)
    productstring = ''

    for item in cart_details:
        product = item['product']

        x = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total'])

        productstring = productstring + x

    context = {
        'cart_details': cart_details,
        'productstring': productstring
    }

    return render(request, 'cart.html', context)

# function for successful orders
def success(request):
    cart = Cart(request)
    cart.clear()
    
    return render(request, 'success.html')