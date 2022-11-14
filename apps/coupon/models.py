from django.db import models

# Coupons Functions

class Coupon(models.Model):
    # makes sure the discount code is unique
    code = models.CharField(max_length=50, unique=True)

    # allows for customised numerical value for discounts
    value = models.IntegerField()

    # allows discounts to be valid for a limited amount of time
    active = models.BooleanField(default=True)

    # sets a maximum of discounts
    num_available = models.IntegerField(default=1)

    # tracks the number of discounts used
    num_used = models.IntegerField(default=0)

    # function returns discount code
    def _str_(self):
        return self.code

    # function to determine if a discount is valid
    def can_use(self):
        is_active = True

        # returns innactive when discount is inactive
        if self.active == False:
            is_active = False

        # returns innactive when discount has been used
        if self.num_used >= self.num_available and self.num_available !=0:
            is_active = False

        return is_active

    # function to track when a discount is used
    def use(self):
        # when a discount is used the number of discounts used is increased
        self.num_used = self.num_used + 1

        # if all available discounts have been used the discount will not be applied (invalid)
        if self.num_used == self.num_available:
            self.active = False
        # this is then saved
        self.save()
