import random
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Product, Category, ProductReview
from .forms import ReviewForm, EditReviewForm
from .forms import AddProductForm, EditProductForm
from django.db.models import Q
from apps.cart.cart import Cart


# search  function
def search(request):
    query = request.GET.get('query')

    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)

    if instock:
        products = products.filter(num_available__gte=1)

    context = {

        'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'searchbar.html', context)


# displays add product page using django UpdateView
class add_product(SuccessMessageMixin, CreateView):

    # using review model
    model = Product

    # using review Form
    form_class = AddProductForm

    # using html template to display comments
    template_name = 'add_product.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = "A new product has been added !"


# displays edit product page using django UpdateView
class edit_product(SuccessMessageMixin, UpdateView):
    # using review model
    model = Product

    # using review Form
    form_class = EditProductForm

    # using html template to display comments
    template_name = 'edit_product.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = "A product has been edited !"


# displays delete product page using django DeleteView
class delete_product(SuccessMessageMixin, DeleteView):

    # using Post model
    model = Product

    # using html template to display edit post page
    template_name = 'delete_product.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " A product was deleted from the E-store "

    # function to show success message for delete view
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_product, self).delete(request, *args, **kwargs)

    # if post is deleted user is returned to homepage
    success_url = reverse_lazy('home')


# view product page functions
def view_product(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    product.num_visits = product.num_visits + 1
    product.last_visit = datetime.now()
    product.save()

    # displays related products
    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))

    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    # where there is a variant of the product the parent product redirects to the product page
    if product.parent:
        return redirect('view_product', category_slug=category_slug, slug=product.parent.slug)

    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)

    # product image is displayed
    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    cart = Cart(request)

    # if product is in stock then it is added to the cart
    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False

    context = {
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products
    }

    return render(request, 'view_product.html', context)


# category view function
def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)
    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_details.html', context)
