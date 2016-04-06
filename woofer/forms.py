from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Profile, Dog, Event, EventAttendance
from django.contrib.auth.forms import UserChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)

class DogForm(ModelForm):
    """ Form for adding/editing a dog profile. """
    class Meta:
        model = Dog
        exclude = ('id','owner',)
        widgets = {
            'id' : forms.HiddenInput(),
            'owner' : forms.HiddenInput()
        }

class EditEventForm(ModelForm):
    """ Form for editing an event. """
    class Meta:
        model = Event
        fields = '__all__'

class CreateEventForm(ModelForm):
    """ Form for creating an event. """
    class Meta:
        model = Event
        exclude = ('user', )
        # We don't want these to be changed so hide them from the user
        widgets = {
            'user' : forms.HiddenInput()
        }
        
class EventAttendanceForm(forms.Form):
    """ Form for attending an event. """
    # dog_field = None
  
    def __init__(self, user, current_event, *args, **kwargs):
        super(EventAttendanceForm, self).__init__(*args, **kwargs)
        # Get all the dogs attending this event so we don't add them to the
        # list of dogs that can be added
        dogs_ids_attending_event = EventAttendance.objects.all() \
                .filter(event = current_event) \
                .values('dog')
        
        self.fields['dog_field'] = forms.ModelChoiceField(
                queryset=Dog.objects.filter(owner=user) \
                            .exclude(id__in=dogs_ids_attending_event),
                required=True,
                label='Dog',
                empty_label=None)
                
                
class RemoveAttendanceForm(forms.Form):
    """ Form for attending an event. """
    # dog_field = None
  
    def __init__(self, user, current_event, *args, **kwargs):
        super(RemoveAttendanceForm, self).__init__(*args, **kwargs)
        # Get all the dogs attending this event so we don't add them to the
        # list of dogs that can be added
        dogs_ids_attending_event = EventAttendance.objects.all() \
                .filter(event = current_event) \
                .values('dog')
        
        self.fields['dog_field'] = forms.ModelChoiceField(
                queryset=Dog.objects.filter(owner=user) \
                            .filter(id__in=dogs_ids_attending_event),
                required=True,
                label='Dog',
                empty_label=None)

class ProfileForm(ModelForm):
    """ Form for editing and creating user woofer profiles. """
    class Meta:
        model = Profile
        exclude = ('user', )
        
class UserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
