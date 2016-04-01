from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from .forms import EventForm
from .models import Event


def event_view(request):
    """ This is the view for the event details. """
    
    event = None
    
    return render(request, 'woofer/event_details.html', { 'event' : event })
    
    
def view_event_list(request):
    """ This view provides a list of events not in the past sorted by their date. """
    
    events = Event.objects.all()
    
    return render(request, 'woofer/event_list.html', { 'events' : events })