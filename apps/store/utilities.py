from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from apps.order.views import render_to_pdf
from django.http import HttpResponse


# fucntion to decrease product quantity after it has been purchased
def decrement_product_quantity(order):
    for item in order.items.all():
        product = item.product
        product.num_available = product.num_available - item.quantity
        product.save()


# fucntion to send order confirmation
def send_order_confirmation(self, order):
    subject = 'Order confirmation'
    from_email = 'estoreorders83@gmail.com'
    to = [order.email]
    text_content = 'Your order was successful!'
    html_content = render_to_string('order_confirmation.html', {'order': order})

    pdf = render_to_pdf('order_pdf.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    if pdf:
        name = 'order_%s.pdf' % order.id
        msg.attach(name, pdf, 'application/pdf')

    msg.send()
