from django.db import models


# category model
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    # changes 'Categorys' to Categories in the admin section, orders categories
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('ordering', )

    # Category names are displayed in the admin
    def __str__(self):
        return self.title


# products model
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    # orders products by the date they were added
    class Meta:
        ordering = ('-date_added',)

    # Product names are displayed in the admin
    def __str__(self):
        return self.title
