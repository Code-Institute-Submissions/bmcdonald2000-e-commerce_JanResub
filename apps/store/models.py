from io import BytesIO
from django.core.files import File
from PIL import Image
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
    image = models.ImageField(upload_to="media/images/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="media/images/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # orders products by the date they were added
    class Meta:
        ordering = ('-date_added',)

    # Product names are displayed in the admin
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.thumbnails(self.image)

        super().save(*args, **kwargs)

    # create thumbnails
    def thumbnails(self, image, size=(300, 200)):

        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
