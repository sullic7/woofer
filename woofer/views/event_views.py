from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView

from django.http import HttpResponseRedirect
from ..forms import EventForm
from ..models import Event


def view_event(request, eventid):
    """ This is the view for the event details. """
    event = Event.objects.get(id=eventid)
    return render(request, 'woofer/events/event_details.html', { 'event' : event })
    
    
def view_event_list(request):
    """ This view provides a list of events not in the past sorted by their date. """
    
    events = Event.objects.all()

    return render(request, 'woofer/events/event_list.html', { 'events' : events })
    
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
    """ Display and handel a form for editing events """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # for some reason django is not putting the object id in the form
            # so if we don't manually update the id it will insert a new object
            new_event = form.save(commit=False)
            new_event.id = eventid
            new_event.save()
            
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
    else:
        event = Event.objects.get(id = eventid)
        form = EventForm(instance = event)
        
        return render(request, 'woofer/show_form.html', {
            'form' : form,
            'message' : None,
            'form_action' : reverse('edit-event', args=[eventid])
        } )
