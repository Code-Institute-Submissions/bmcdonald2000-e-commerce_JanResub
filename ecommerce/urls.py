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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.cart.views import cart
from apps.core.views import home, contact, about_us
from apps.store.views import view_product, category_details

from apps.store.api import add_to_cart, delete_from_cart, Checkout

# url configarations for apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart, name='cart'),
    path('', home, name='home'),
    path('Contact_Us/', contact, name='contact'),
    path('About_Us/', about_us, name='about_us'),

    # Store Paths
    path('<slug:category_slug>/<slug:slug>/View_Details/', view_product, name='view_product'),
    path('<slug:slug>/View_Details/', category_details, name='category_details'),

    # API paths
    path('api/add_to_cart/', add_to_cart, name='add'),
    path('api/delete_from_cart/', delete_from_cart, name='delete'),
    path('api/checkout/', Checkout, name='checkout_api'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
