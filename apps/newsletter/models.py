from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Subscriber model
class Subscriber(models.Model):
    # subscriber email, date and confirmation details are stored
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    # email and confirmation details are retruned as string
    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


# Newsletter model so that the admin can send newsletters from the admin
class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = RichTextField(blank=False, null=False)

    # newsletter subject and creation date displayed in admin
    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    # function to send newsletter to users
    def send(self, request):
        contents = self.contents
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="https://tranquil-temple-81228.herokuapp.com/delete/?email={subscriber.email}&conf_num={subscriber.conf_num}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            sg.send(message)
