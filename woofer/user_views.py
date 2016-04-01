from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import WooferUser


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
                return HttpResponseRedirect('/index')
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
            form.save()
            print("We should be logging in the user here")
            return HttpResponseRedirect('/index')
    else:
        form = UserCreationForm()
    
    
    return render(request, 'woofer/create_user.html', {
        'form' : form,
        'message': message
    })
    

def logout_view(request):
    """ This view handels loggign the user out. """
    
    logout(request)
    return render(request, 'woofer/index.html')



def user_view(request, userid):
    """ This is the view for the user details. """
    
    user = WooferUser.objects.get(id=userid)
    
    return render(request, 'woofer/user_profile.html', { 'user' : user } )
    
    