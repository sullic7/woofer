from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from ..forms import LoginForm, ProfileForm
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
            print("form is valid.")
            user =  authenticate(username=form.cleaned_data['username'],
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
    
    
    return render(request, 'woofer/login.html', {
        'form' : form,
        'message': message
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
        'form_action' : reverse('create-user')
    })
    
@login_required
def view_profile(request):
    """ Redirect the user to the view user screen for their userid. """
    return HttpResponseRedirect(reverse('view-user', args=[request.user.id]))

def logout_view(request):
    """ This view handels loggign the user out. """
    logout(request)
    return render(request, 'woofer/index.html')


def view_user(request, userid):
    """ This is the view for the user details. """
    user_to_view = User.objects.get(id = userid)
    profile = Profile.objects.get(user = user_to_view)
    dogs = Dog.objects.all().filter(owner = user_to_view)

    return render(request, 'woofer/view_user.html', 
    { 
        'profile' : profile,
        'dogs' : dogs
    } )

    
def edit_user(request, userid):
    """ This view dispalys a form for the user to edit their profile """
    # first we need to get the user model we're editing to populate the form
    # this should be the logged in user, but right now we'll just make it the one
    # specefied in the URL
    woofer_user = User.objects.get(id = userid)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    else:
        # populate the form with the values in the internal dict of the user object
        form = ProfileForm(initial = woofer_user.__dict__)
        
        return render(request, 'woofer/show_form.html', { 
            'form' : form,
            'message' : None,
            'form_action' : reverse('edit-user', args=[userid])
        } )