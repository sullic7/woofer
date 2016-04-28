""" This module holds the views pertaining to the index page."""
from django.shortcuts import render
from django.db.models import Count

from ..models import Event, EventAttendance, Dog

def index(request):
    """ Display the home page. If the user is logged in display a list of
    the events they own and a list of events their attending.
    """
    owned_events = None
    attending_events = None
    if request.user.is_authenticated():
        owned_events = Event.objects.all().filter(user=request.user)
        owned_dog_ids = Dog.objects.all().filter(owner=request.user)

        attending_event_ids = EventAttendance.objects.all().\
            filter(dog_id__in=owned_dog_ids).values('event_id')

        attending_events = Event.objects.annotate(Count('eventattendance'))\
            .all().filter(id__in=attending_event_ids)

    return render(request, 'woofer/index.html',
                  {
                      'owned_events' : owned_events,
                      'attending_events' : attending_events
                  })
