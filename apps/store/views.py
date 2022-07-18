from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# producdetailsview.

def view_product(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'view_product.html', context)


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_details.html', context)
