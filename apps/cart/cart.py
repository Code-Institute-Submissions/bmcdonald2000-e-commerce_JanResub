from django.conf import settings

from apps.store.models import Product


# Cart function
class Cart(object):
    # function to remove items from the basket after 12 hours
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # if the cart is empty a new session will be started
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # function to iterate through the products
    def __iter__(self):
        product_ids = self.cart.keys()
        clean_product = []

        for p in product_ids:
            clean_product.append(p)

            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total'] = item['price'] * int(item['quantity'])

            yield item

    # function to calculate product length
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # function to update the cart
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        print('Product_id:', product_id)

        # if a product id, doesnt exist one is created
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}

        # quantity of items in the cart is updated
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        # save cart
        self.save()

    # function to track product inventory
    def has_product(self, product_id):
        if str(product_id) in self.cart:
            return True
        else:
            return False

    # function to delete items from cart
    def delete(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # function to update and save the browser session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # function to clear basket on checkout
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    # fucntion to calculate total quantity in the cart
    def total_length(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    #  function to calculate total cost of the cart
    def total_cost(self):
        return sum(float(item['total']) for item in self)
