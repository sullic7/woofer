from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.http import HttpResponseRedirect
import forms
import navigationbar

def index(request):
    """ I'm a doc string and every method should have me. I tell you what
    I do. In this case I'm the index."""
    
    some_words = "you can pass data to a templte form a view like this!"

    return render(request, 'woofer/index.html', 
        { 'some_words' : some_words }
    )

    
def login(request):
    """ This is the view that is called when sumbitting the login form. 
    We authenticate the user here and log them inself.
    """
    # If login fails this is where we will put an error message to display
    message = None
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print("We should be logging in the user here")
            return HttpResponseRedirect('/index')
        else:
            message = "Invalid username or password"
    else:
        form = AuthenticationForm()
    
    
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

def user_view(request):
    """ This is the view for the user form. """
    
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = forms.UserForm()
    
    return render(request, 'woofer/user_profile.html', {'form':form} )
    
def dog_view(request):
    """ This is the view for the dog form. """

    if request.method == 'POST':
        form = forms.DogForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = forms.DogForm()
    
    return render(request, 'woofer/dog_profile.html', {'form':form})
    
def event_view(request):
    """ This is the view for the event form. """

    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = forms.EventForm()
    
    return render(request, 'woofer/event_creation.html', {'form':form})