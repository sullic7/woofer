from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect


def index(request):
    """ I'm a doc string and every method should have me. I tell you what
    I do. In this case I'm the index."""
    
    some_words = "you can pass data to a templte form a view like this!"

    return render(request, 'woofer/index.html', 
        { 'some_words' : some_words }
    )
