"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django imports

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from apps.cart.webhook import webhook
from apps.cart.views import cart_details, success, fail
from apps.core.views import home, contact, about_us, order_confirmation
from apps.order.views import admin_order_pdf
from apps.store.views import view_product, category_details, search
from apps.store.views import add_product, edit_product, delete_product
from apps.store.views import ReviewView, EditReviewView, DeleteReviewView
from apps.newsletter.views import new
from apps.userprofile.views import signup, myaccount, EditAccountView
from apps.userprofile.views import DeleteAccountView

from apps.coupon.api import valid_coupon
from apps.store.api import add_to_cart, delete_from_cart
from apps.store.api import checkout_session
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views


# url configarations for apps
urlpatterns = [
    path('admin/order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('webhooks/', webhook, name='hook'),
    path('cart/', cart_details, name='cart'),
    path('cart/success/', success, name='success'),
    path('cart/cancel/', fail.as_view(), name='cancel'),
    path('', home, name='home'),
    path('Contact_Us/', contact, name='contact'),
    path('About_Us/', about_us, name='about_us'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),

    # user paths
    path('myaccount/', myaccount, name='myaccount'),
    path('verification/', include('verify_email.urls')),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('myaccount/Edit_profile/<int:pk>/', EditAccountView.as_view(),
         name='profile'),
    path('myaccount/Delete_phone_number/<int:pk>/', DeleteAccountView.as_view(),
         name='delete_profile'),
    path('add_product/', add_product,
         name='product'),
    path('edit_product/<int:pk>/', edit_product.as_view(),
         name='edit_product'),
    path('delete_product/<int:pk>/', delete_product.as_view(),
         name='delete_product'),
    path('new/', new, name='new'),


    # API paths
    path('api/add_to_cart/', add_to_cart, name='add'),
    path('api/delete_from_cart/', delete_from_cart, name='delete'),
    path('api/checkout_session/', checkout_session, name='checkout_session'),
    path('api/valid_coupon/', valid_coupon, name='valid_coupon'),

    # Store Paths
    path('<slug:category_slug>/<slug:slug>/', view_product, name='view_product'),
    path('<slug:slug>/', category_details, name='category_details'),
    path('<slug:category_slug>/<slug:slug>/add_review/', ReviewView.as_view(), name='reviews'),
    path('<slug:category_slug>/<slug:slug>/<int:pk>/edit_review/', EditReviewView.as_view(), name='edit_review'),
    path('<slug:category_slug>/<slug:slug>/<int:pk>/delete_review/', DeleteReviewView.as_view(), name='delete_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler fuction for custom 404 page
handler404 = "ecommerce.views.page_not_found_view"
