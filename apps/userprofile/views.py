from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, UserprofileForm

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

            # then signed up the user is redirected to the homepage
            return redirect('home')

    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()

    return render(request, 'signup.html', {'form': form, 'userprofileform': userprofileform})

# the user must be logged in to view their account
@login_required
def myaccount(request):
    return render(request, 'myaccount.html')
