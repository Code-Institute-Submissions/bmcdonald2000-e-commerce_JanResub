from django.contrib.auth.models import User
from django.db import models


# function to return the authorised users data
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=8, blank=True, null=True)
    city = models.TextField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.username


User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])
