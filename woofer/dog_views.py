from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from .forms import DogForm
from .models import Dog


def dog_view(request, dogid):
    """ This is the view for the dog details. """

    dog = Dog.objects.get(id=dogid)
    
    return render(request, 'woofer/dog_profile.html', { 'dog' : dog })
