import random
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
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



@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            # adds a message if the form is successful
            messages.success(request, 'A new product has been added !')
            return redirect(reverse('view_product', args=[product.category.slug,product.slug]))
        else:
            # adds a message if form is unsuccessful
            messages.error(request, 'Failed to add product Check the form is valid')
    else:
        form = AddProductForm()

    # using html template to display products
    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# displays edit product page using django UpdateView
class edit_product(SuccessMessageMixin, UpdateView):
    # using review model
    model = Product

    # using review Form
    form_class = EditProductForm

    # using html template to edit products
    template_name = 'edit_product.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = "A product has been edited !"


# displays delete product page using django DeleteView
class delete_product(SuccessMessageMixin, DeleteView):

    # using Post model
    model = Product

    # using html template to delete product
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


# displays reviews using django CreateView
class ReviewView(SuccessMessageMixin, CreateView):

    # using review model
    model = ProductReview

    # using review Form
    form_class = ReviewForm

    # using html template to display comments
    template_name = 'reviews.html'

    # valid form id used to add username to comment
    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    # adds a message if the form is success using SuccessMessageMixin
    success_message = "Thanks for leaving your review !"


# displays edit review page using django UpdateView
class EditReviewView(SuccessMessageMixin, UpdateView):

    # using Post model
    model = ProductReview

    # using EditForm
    form_class = EditReviewForm

    # using html template to display edit post page
    template_name = 'edit_review.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Yay !! your review has been updated "


# displays delete review page using django UpdateView
class DeleteReviewView(SuccessMessageMixin, DeleteView):

    # using Post model
    model = ProductReview

    # using html template to display edit post page
    template_name = 'delete_review.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Your review was deleted from the E-store "

    # function to show success message for delete view
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteReviewView, self).delete(request, *args, **kwargs)

    # if post is deleted user is returned to homepage
    success_url = reverse_lazy('home')
