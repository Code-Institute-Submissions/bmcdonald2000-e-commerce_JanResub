from django.conf import settings


# Cart function
class Cart(object):
    # function to remove items from the basket after 12 hours
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SESSION_COOKIE_AGE)

        # if the cart is empty a new session will be started
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # function to update the cart
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        # if a product id, doesnt exist one is created.
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':price, 'id':product_id}

        # quantity of items in the cart is updated
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1

        self.save()

    # function to update and save the browser session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
