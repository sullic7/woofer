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
  
    def __init__(self, user, *args, **kwargs):
        super(EventAttendanceForm, self).__init__(*args, **kwargs)
        self.fields['dog_field'] = forms.ModelChoiceField(
                queryset=Dog.objects.filter(owner=user),
                required=True,
                label='Dog')
        
        # dogs = Dog.objects.all().filter(owner = user)
        # DOGS = []
        # for dog in dogs:
        #     DOGS.append((dog.id, dog.name))
        # DOGS = tuple(DOGS) 
        # self.dog_field = forms.ChoiceField(choices=DOGS, required=True, label='Dogs')
        
    
class ProfileForm(ModelForm):
    """ Form for editing and creating user woofer profiles. """
    class Meta:
        model = Profile
        exclude = ('user', )
        
class UserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
