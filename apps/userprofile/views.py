from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from verify_email.email_handler import send_verification_email
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

        # if the form is valid then the users details are saved and a verification link is sent
        if form.is_valid() and userprofileform.is_valid():

            user = form.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()
            
            messages.success(request,
                             'Verify your email to complete registration')
            inactive_user = send_verification_email(request, form)

    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()

    return render(request, 'signup.html', {'form': form, 
                                           'userprofileform': userprofileform})


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

    # if form is completly successfully then user is returned to their account page
    success_url = reverse_lazy('myaccount')

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Your account is now up to date !"


# displays delete phone number page using django UpdateView
class DeleteAccountView(SuccessMessageMixin, DeleteView):

    # using Post model
    model = Userprofile

    # using ProfilePageForm
    form_class = DeleteForm

    # using html template to display edit post page
    template_name = 'delete_profile.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = "Your number has been deleted from the E-store"

    # function to show success message for delete view
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteAccountView, self).delete(request, *args, **kwargs)

    # if post is deleted user is returned to their account
    success_url = reverse_lazy('myaccount')
