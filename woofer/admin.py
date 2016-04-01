from django.contrib import admin
from .models import WooferUser, Dog, Event, EventAttendance

# Register your models here.
admin.site.register(WooferUser)
admin.site.register(Dog)
admin.site.register(Event)
admin.site.register(EventAttendance)