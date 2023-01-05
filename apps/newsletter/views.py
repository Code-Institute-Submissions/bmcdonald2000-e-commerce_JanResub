from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# fucntion to generate a random confirmation code
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
# function for new subscriber confirmation link
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=sub.email,
            subject='Welcome to the E-store newsletter!',
            html_content=' If you would like to be removed from the mailing list please\
                <a href="https://tranquil-temple-81228.herokuapp.com/Contact_Us/"> \
                click here to contact the Estore Team</a>.')
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'parts/newsletter.html', {'email': sub.email,
                                                         'action': 'added',
                                                         'form': SubscriberForm()})
    else:
        return render(request, 'parts/newsletter.html',
                      {'form': SubscriberForm()})
