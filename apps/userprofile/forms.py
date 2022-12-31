from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile


# form for user profile
class UserprofileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserprofileForm, self).__init__(*args, **kwargs)

        self.fields['address'].widget.attrs['class'] = 'input'
        self.fields['postcode'].widget.attrs['class'] = 'input'
        self.fields['city'].widget.attrs['class'] = 'input'
        self.fields['phone'].widget.attrs['class'] = 'input'

    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user',)


# user sign up form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    # function to improve signup form asethetic
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'
        self.fields['first_name'].widget.attrs['class'] = 'input'
        self.fields['last_name'].widget.attrs['class'] = 'input'

    # meta data for signup form
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# creates an edit account form using  a model
class EditAccountForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using Post model
        model = Userprofile

        # fields that will be used for the form
        fields = ('address', 'postcode', 'city', 'phone')

        # basic controls/styling for the form fields
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Enter Your Full Address'}),
            'postcode': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder':
                                          'Enter your Postcode'}),
            'city': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'Enter Your City'}),
            'phone': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'Enter Your Phone Number'}),
        }


# creates an delete number form using  a model
class DeleteForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using Post model
        model = Userprofile

        # fields that will be used for the form
        fields = ('address', 'postcode', 'city',
                  'phone')

        # basic controls/styling for the form fields
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Enter Your Full Address'}),
            'postcode': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder':
                                          'Enter your Postcode'}),
            'city': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'Enter Your City'}),
            'phone': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'Enter Your Phone Number'}),
        }
