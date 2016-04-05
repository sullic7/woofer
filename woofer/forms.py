from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Profile, Dog, Event, EventAttendance

class LoginForm(forms.Form):
    username = forms.CharField(label='Username1', max_length=100)
    password = forms.CharField(label='Password2', widget=forms.PasswordInput, max_length=100)

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
    
class ProfileForm(ModelForm):
    """ Form for editing and creating user woofer profiles. """
    class Meta:
        model = Profile
        fields = '__all__'
