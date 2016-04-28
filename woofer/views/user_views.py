""" This module holds the views pertaining to Users."""
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from ..forms import LoginForm, ProfileForm, UserDetailsForm
from ..models import Profile, Dog


def login_view(request):
    """ This is the view that is called when sumbitting the login form.
    We authenticate the user here and log them inself.
    """
    # If login fails this is where we will put an error message to display
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = None
        # if the form validation passed try to authenticate the user
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                message = "The password is valid, but the account has been disabled!"
        else:
            message = "Invalid username or password"
    else:
        form = LoginForm()

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : message,
        'form_action' : reverse('login'),
        'title' : "Login"
    })

def create_user(request):
    """ This view handels displaying and processing a user creation form """
    message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This creates a new User in the database
            new_user = form.save()
            # now we create a new blank profile, link it to the new user and save it
            new_profile = Profile()
            new_profile.user = new_user
            new_profile.save()
            return HttpResponseRedirect('/index')
    else:
        form = UserCreationForm()

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : message,
        'form_action' : reverse('create-user'),
        'title' : "Create Account"
    })

@login_required
def view_profile(request, userid=None):
    """ Redirect the user to the view user screen for their userid. """
    # Show the currently logged in user's profile if none is specified
    if userid is None:
        user = request.user
    else:
        user = User.objects.get(id=userid)
    profile = Profile.objects.get(user=user)
    dogs = Dog.objects.all().filter(owner=user)

    return render(request, 'woofer/view_profile.html',
                  {
                      'profile' : profile,
                      'dogs' : dogs
                  })

def logout_view(request):
    """ This view handels loggign the user out. """
    logout(request)
    return render(request, 'woofer/index.html')

def view_user(request, userid):
    """ This is the view for the user details. """
    user_to_view = User.objects.get(id=userid)
    profile = Profile.objects.get(user=user_to_view)
    dogs = Dog.objects.all().filter(owner=user_to_view)

    return render(request, 'woofer/view_user.html',
                  {
                      'profile' : profile,
                      'dogs' : dogs
                  })

def edit_user(request, userid):
    """ Display a ChangeUser form to the user and handel it when it comes back. """
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            # we're going to update the first_name, last_name, and email fields of this object
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return HttpResponseRedirect(reverse('view-profile', args=[userid]))
    else:
        form = UserDetailsForm(instance=request.user)

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : None,
        'form_action' : reverse('edit-user', args=[userid]),
        'title' : "Edit Account"
    })

def edit_profile(request, userid):
    """ This view dispalys a form for the user to edit their profile """
    woofer_user = User.objects.get(id=userid)
    current_profile = Profile.objects.get(user=woofer_user)
    if woofer_user.id != request.user.id:
        return HttpResponseRedirect(reverse('view-profile', args=[userid]))

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            # copy the ID of the User's current profile to the new profile so
            # Django performs an update when we call .save()
            new_profile.id = current_profile.id
            new_profile.user = woofer_user
            new_profile.save()
            return HttpResponseRedirect(reverse('view-profile', args=[userid]))
    else:
        form = ProfileForm(instance=current_profile)

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : None,
        'form_action' : reverse('edit-profile', args=[userid]),
        'title' : "Edit Profile"
    })

def change_password(request):
    """ This view displays and handels an edit password form. """
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('view-profile', args=[request.user.id]))
        else:
            print "form not valid"
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : None,
        'form_action' : reverse('change-password'),
        'title' : "Change Password"
    })
