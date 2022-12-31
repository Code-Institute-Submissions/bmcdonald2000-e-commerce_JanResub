from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Userprofile
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm, UserprofileForm, EditAccountForm, DeleteForm


# user signup form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userprofileform = UserprofileForm(request.POST)

        # if the form is valid then the users details are saved
        if form.is_valid() and userprofileform.is_valid():
            user = form.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()

            login(request, user)

            # adds a message if the signup is successful using SuccessMessageMixin
            success_message = "You are now an E-store member !"

            # if user is signedup they are returned to the homepage
            success_url = reverse_lazy('home')
    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()

    return render(request, 'signup.html', {'form': form, 'userprofileform': userprofileform})


# the user must be logged in to view their account
@login_required
def myaccount(request):
    return render(request, 'myaccount.html')


# displays edit profile page using django UpdateView
class EditAccountView(SuccessMessageMixin, UpdateView):

    # using UserProfile model
    model = Userprofile

    # displayed on html template page
    template_name = 'edit_account.html'

    # using ProfilePageForm
    form_class = EditAccountForm

    # if form is completly successfully then user is returned to the home page
    success_url = reverse_lazy('myaccount')

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Your account is now up to date !"