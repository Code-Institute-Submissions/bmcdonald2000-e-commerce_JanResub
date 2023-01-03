from django.shortcuts import render
from django.http import HttpResponse
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
            subject='Newsletter Confirmation',
            html_content='Welcome to the E-store newsletter! \
                To complete the process \
                <a href="https://tranquil-temple-81228.herokuapp.com/confirm/?email={}&conf_num={}"> click here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('https://tranquil-temple-81228.herokuapp.com/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'parts/newsletter.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()}) 
    else:
        return render(request, 'parts/newsletter.html', {'form': SubscriberForm()})


# funciton to confirm subscription
def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'parts/newsletter.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'parts/newsletter.html', {'email': sub.email, 'action': 'denied'})


# fuction to unsubscribe
def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'parts/newsletter.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'parts/newsletter.html', {'email': sub.email, 'action': 'denied'})