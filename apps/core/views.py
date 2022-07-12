from django.shortcuts import render
from apps.store.models import Product


# Home view
def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'home.html', context)


# Contact view
def contact(request):
    return render(request, 'contact_us.html')
