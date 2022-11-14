import json
from django.http import JsonResponse
from .models import Subscriber

# function to add a subcriber
def api_add_subscriber(request):
    # data from the form is used
    data = json.loads(request.body)
    # users email is retreived
    email = data['email']

    # the user is added as a subscriber
    s = Subscriber.objects.create(email=email)

    # this data is then returned as json to the fornt end via the api
    return JsonResponse({'success': True})