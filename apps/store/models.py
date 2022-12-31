from io import BytesIO
from django.urls import reverse
from django.core.files import File
from PIL import Image
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


# category model
class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    # changes 'Categorys' to Categories in the admin section, orders categories
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('ordering', )

    # Category names are displayed in the admin
    def __str__(self):
        return self.title

    # Function to get the absolute url for categories
    def get_absolute_url(self):
        return '/%s/' % (self.slug)


# products model
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    num_available = models.IntegerField(default=3)
    num_visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # orders products by the date they were added
    class Meta:
        ordering = ('-date_added',)

    # Product names are displayed in the admin
    def __str__(self):
        return self.title


    # Function to get the absolute url for the products
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.thumbnails(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''

    # Function to create thumbnails
    def thumbnails(self, image, size=(300, 200)):

        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

        # function to get the product ratings
    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        # if there are reviews, they are shown
        if self.reviews.count() > 0:
            return total/self.reviews.count()
        # else the user is informed that there are no reviews
        else:
            return 0


# fucntion to add multiple product images
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)

    # saves product images
    def save(self, *args, **kwargs):
        self.pthumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    # creates thumbnails for product images
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


# Function for product review
class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    name = models.CharField( max_length=255)
    author = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    stars = models.TextField(choices=RATING_CHOICES, default='3')
    date_added = models.DateTimeField(auto_now_add=True)

    # function to return data as string in the django admin
    def __str__(self):
        return '%s - %s' % (self.product.title, self.name)

    # redirects user to the product page if the form is successful
    def get_absolute_url(self):
        return reverse('view_product', args=(self.product.category.slug, self.product.slug, ))

