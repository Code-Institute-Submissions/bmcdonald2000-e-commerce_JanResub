from django.shortcuts import render
from apps.store.models import Product


# Home view
def home(request):
    # only featured products are shown on the homepage
    products = Product.objects.filter(featured=True)

    context = {
        'products': products
    }

    return render(request, 'home.html', context)


# Contact view
def contact(request):
    return render(request, 'contact_us.html')


# About us view
def about_us(request):
    return render(request, 'about_us.html')
