from django.contrib import admin
from django import forms
from .models import Profile, Dog, Event, EventAttendance
# Register your models here.
admin.site.register(Profile)
admin.site.register(Dog)
admin.site.register(Event)
admin.site.register(EventAttendance)
