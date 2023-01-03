from django.contrib import admin
from .models import Subscriber, Newsletter


# function to send newsletter
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)


send_newsletter.short_description = "Send Selected Newsletter to Subscribers"


# adds send newsletter button to admin
class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]


# Registers the subscriber and newsletter models in the admin
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
