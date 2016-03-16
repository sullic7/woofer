from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from models import WooferUser, Dogs, Events

class LoginForm(ModelForm):
    """ Form for user login. """
    class meta:
        model = WooferUser
        fields = ['user']

class UserForm(ModelForm):
    """ Form for creating/editing a user profile. """
    class Meta:
        model = WooferUser
        fields = '__all__'
        
class DogForm(ModelForm):
    """ Form for adding/editing a dog profile. """
    class Meta:
        model = Dogs
        fields = '__all__'
        
class EventForm(ModelForm):
    """ Form for editing/creating and event. """
    class Meta:
        model = Events
        fields = '__all__'