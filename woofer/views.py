from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
import forms

def index(request):
    """ I'm a doc string and every method should have me. I tell you what
    I do. In this case I'm the index."""
    
    some_words = "you can pass data to a templte form a view like this!"
    
    return render(request, 'woofer/index.html', 
        { 'some_words' : some_words }
    )
    
def user_view(request):
    """ This is the view for the user form. """
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = forms.UserForm()
    
    return render(request, 'woofer/user_profile.html', {'form':form})
    
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