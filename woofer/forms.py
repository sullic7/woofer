from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import WooferUser, Dogs, Events

# class LoginForm(ModelForm):
#     """ Form for user login. """
#     class meta:
#         model = WooferUser
#         fields = [User.username, User.password]

# class UserForm(ModelForm):
#     """ Form for creating/editing a user profile. """
#     class Meta:
#         model = WooferUser
#         fields = [User.username, User.password, User.first_name, User.last_name,
#                     User.email, 'phone_number', 'zipcode', 'birthday']
        
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