from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from .forms import DogForm


def dog_view(request):
    """ This is the view for the dog details. """

    dog = None
    
    return render(request, 'woofer/dog_profile.html', { 'dog' : dog })
