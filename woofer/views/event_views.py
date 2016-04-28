from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

from django.http import HttpResponseRedirect
from ..forms import EditEventForm, CreateEventForm, EventAttendanceForm, \
RemoveAttendanceForm
from ..models import Event, EventAttendance, Dog


def view_event(request, eventid):
    """ This is the view for the event details. """
    event = Event.objects.annotate(Count('eventattendance')).get(id=eventid)
    
    dog_ids = EventAttendance.objects.all().filter(event_id = event.id).values('dog')
    dogs = Dog.objects.all().filter(id__in=dog_ids)

    attend_form = None
    remove_form = None
    if request.user.is_authenticated():
        attend_form = EventAttendanceForm(request.user, event)
        remove_form = RemoveAttendanceForm(request.user, event)

    return render(request, 'woofer/events/event_details.html',
                  {
                      'event' : event,
                      'dogs' : dogs,
                      'attend_form' : attend_form,
                      'remove_form' : remove_form
                  })
def view_event_list(request):
    """ This view provides a list of events not in the past sorted by their date. """
    events = Event.objects.all()
    return render(request, 'woofer/events/event_list.html', {'events' : events})

@login_required
def create_event(request):
    """ Displays a form for creating an event """
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            # assign the new event to the current user
            new_event.user = request.user
            new_event.save()
            return HttpResponseRedirect(reverse('view-event', args=[new_event.id]))
    else:
        form = CreateEventForm()
    return render(request, 'woofer/show_form.html', {
        'form' : form,
        'form_action' : reverse('create-event'),
        'title' : "Create Event"
    })
def edit_event(request, eventid):
    """ Display and handel a form for editing events """
    event = Event.objects.get(id=eventid)
    # Check that the user can edit this event
    if event.user.id != request.user.id:
        return HttpResponseRedirect(reverse('view-event', args=[eventid]))
    if request.method == 'POST':
        form = EditEventForm(request.POST)
        if form.is_valid():
            # for some reason django is not putting the object id in the form
            # so if we don't manually update the id it will insert a new object
            new_event = form.save(commit=False)
            new_event.id = eventid
            new_event.save()
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
    else:
        form = EditEventForm(instance=event)
        return render(request, 'woofer/show_form.html', {
            'form' : form,
            'message' : None,
            'form_action' : reverse('edit-event', args=[eventid]),
            'title' : "Edit Event"
        })

def attend_event(request, eventid):
    """ Display form for attending an event """
    if request.method == 'POST':
        # check that event still has spots open
        selected_event = Event.objects.annotate(Count('eventattendance')).get(id = eventid)

        if selected_event.eventattendance__count >= selected_event.attendance_cap:
            print("should print a message")
            messages.warning(request, "This event is at capacity so you can not attend it.")
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))

        form = EventAttendanceForm(request.user, selected_event, request.POST)
        if form.is_valid():
            selected_dog = form.cleaned_data['dog_field']
            # Make a new event attendence and save it
            event_attendance = EventAttendance()
            event_attendance.event = selected_event
            event_attendance.dog = selected_dog
            event_attendance.save()
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
        else:
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
    else:
        # This should never happen
        return HttpResponseRedirect(reverse('view-event', args=[eventid]))


def unattend_event(request, eventid):
    """ Display form for attending an event """
    if request.method == 'POST':
        # check that event still has spots open
        selected_event = Event.objects.get(id=eventid)
        form = RemoveAttendanceForm(request.user, selected_event, request.POST)
        if form.is_valid():
            selected_dog = form.cleaned_data['dog_field']
            # Get the event attendance in question and delete it
            event_attendance = EventAttendance.objects \
                        .get(event=selected_event, dog=selected_dog)
            event_attendance.delete()
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
        else:
            return HttpResponseRedirect(reverse('view-event', args=[eventid]))
    else:
        # This should never happen
        return HttpResponseRedirect(reverse('view-event', args=[eventid]))
