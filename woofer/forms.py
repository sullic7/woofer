from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import WooferUser, Dog, Event
        
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username1', max_length=100)
    password = forms.CharField(label='Password2', widget=forms.PasswordInput, max_length=100)

class DogForm(ModelForm):
    """ Form for adding/editing a dog profile. """
    class Meta:
        model = Dog
        fields = '__all__'

class EventForm(ModelForm):
    """ Form for editing/creating and event. """
    class Meta:
        model = Event
        fields = '__all__'
