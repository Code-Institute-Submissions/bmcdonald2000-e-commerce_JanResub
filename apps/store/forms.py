from .models import ProductReview, Product, Category
from django import forms


# creates a query of names from the Category model
choices = Category.objects.all().values_list('title', 'title')
parent_choices = Category.objects.all().values_list('parent', 'parent')

# creates a categories and parent categories lists
categories_dropdown = []
parent_dropdown = []

# any new items are added to the list
for item in choices:
    categories_dropdown.append(item)

for item in parent_choices:
    parent_dropdown.append(item)


# creates an add product form using a model
class AddProductForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using product model
        model = Product

        # fields that will be used for the form
        fields = ('category', 'parent', 'title', 'description', 'price', 'image', 'slug', 'featured', 'thumbnail', 'num_available')

        # products apprear in date order (recent first)
        ordering = ['-date_added']

        # basic controls/styling for the form fields
        widgets = {
            'category':  forms.Select(choices=categories_dropdown,
                                      attrs={'class': 'form-control'}),
            'parent': forms.Select(choices=parent_dropdown,
                                   attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(),
            'num_available': forms.TextInput(attrs={'class': 'form-control'}),
        }


# creates an edit product form using a model
class EditProductForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using product model
        model = Product

        # fields that will be used for the form
        fields = ('category', 'parent', 'title', 'description', 'price', 'image', 'slug', 'featured', 'thumbnail', 'num_available')

        # products apprear in date order (recent first)
        ordering = ['-date_added']

        # basic controls/styling for the form fields
        widgets = {
            'category':  forms.Select(choices=categories_dropdown,
                                      attrs={'class': 'form-control'}),
            'parent': forms.Select(choices=parent_dropdown,
                                   attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(),
            'num_available': forms.TextInput(attrs={'class': 'form-control'}),
        }


# creates an edit form using  a model
class EditReviewForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using review model
        model = ProductReview

        # fields that will be used for the form
        fields = ('content', 'stars')


# creates a review form using a model
class ReviewForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using review model
        model = ProductReview

        # fields that will be used for the form
        fields = ('content', 'stars', 'author')

        # post apprear in date order (recent first)
        ordering = ['-date_added']

        # basic controls/styling for the form fields
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control',
                                           'value': '', 'id': 'username'}),
        }
