from django.db import models


# category model
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    # changes 'Categorys' to Categories in the admin section
    class Meta:
        verbose_name_plural = "Categories"

    # Category names are displayed in the admin
    def __str__(self):
        return self.title

