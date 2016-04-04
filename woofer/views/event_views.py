from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from ..forms import EventForm
from ..models import Event


def event_view(request, eventid):
    """ This is the view for the event details. """
    event = Event.objects.get(id=eventid)
    return render(request, 'woofer/event_details.html', { 'event' : event })
    
    
def view_event_list(request):
    """ This view provides a list of events not in the past sorted by their date. """
    
    events = Event.objects.all()

    return render(request, 'woofer/event_list.html', { 'events' : events })
    
def create_event(request):
    """ SDFJKSDLFJSLKDFJKSDF """
    message = None
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    else:
        form = EventForm()
        
    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'message' : message,
        'form_action' : reverse('create-event')
    } )
    
def edit_event(request, eventid):
    
    event = Event.objects.get(id = eventid)
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    else:
        form = EventForm(initial = event.__dict__)
        
        return render(request, 'woofer/show_form.html', {
            'form' : form,
            'message' : None,
            'form_action' : reverse('edit-event', args=[eventid])
        } )