from django.db import models


# Subscriber model
class Subscriber(models.Model):
    # subscriber email and date of subscription is stored
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    # email is returned as string
    def __str__(self):
        return '%s' % self.email
