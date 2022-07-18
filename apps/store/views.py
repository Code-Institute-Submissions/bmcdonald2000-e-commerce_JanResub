from django.shortcuts import render, get_object_or_404
from .models import Product


# producdetailsview.

def view_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'view_product.html', context)