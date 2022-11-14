from django.shortcuts import render
from apps.store.models import Product, Category
from apps.order.models import Order


# confirmation email view
def order_confirmation(request):
    order = Order.objects.get(pk=1)
    return render(request, 'order_confirmation.html', {'order': order})


# Home view
def home(request):
    # only featured, popoular and recently viewed products are shown on the homepage
    products = Product.objects.filter(featured=True)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }

    return render(request, 'home.html', context)


# Contact view
def contact(request):
    return render(request, 'contact_us.html')


# About us view
def about_us(request):
    return render(request, 'about_us.html')
