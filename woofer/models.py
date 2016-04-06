from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """ This is a profile model of the django user model. More info here 
    https://docs.djangoproject.com/en/1.9/topics/auth/customizing/"""
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    phone_number = models.IntegerField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    # add photo
    
    def __str__(self):
        return self.user.username
        
    def get_formatted_birthday(self):
        if self.birthday:
            return self.birthday.strftime("%m/%d/%y")
    
class Dog(models.Model):
    """ This is a model for dogs which are owned by one user. """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    breed = models.CharField(max_length=100, blank=True, null=True)
    potty_trained = models.BooleanField()
    bio = models.TextField(blank=True, null=True)
    LOW = 'LO'
    MEDIUM = 'MD'
    HIGH = 'HI'
    ACTIVITY_CHOICES = (
            (LOW, 'Not active'),
            (MEDIUM, 'Somewhat active'),
            (HIGH, 'Very active')
        )
    TEMPERAMENT_CHOICES = (
            (LOW, 'Prefers to be left alone'),
            (MEDIUM, 'Good with small groups'),
            (HIGH, 'Good with any size groups')
        )
    activity = models.CharField(max_length=2, choices=ACTIVITY_CHOICES)
    temperament_kids = models.CharField(max_length=2, choices=TEMPERAMENT_CHOICES)
    temperament_dogs = models.CharField(max_length=2, choices=TEMPERAMENT_CHOICES)
    temperament_strangers = models.CharField(max_length=2, choices=TEMPERAMENT_CHOICES)
    # add photo
    
    def __str__(self):
        return self.name
        
    def get_formatted_birthday(self):
        if self.birthday:
            return self.birthday.strftime("%m/%d/%y")
    
class Event(models.Model):
    """ This is a model for events created by one user. """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    description = models.TextField()
    attendance_cap = models.IntegerField(default=0)
    INDOOR = 'I'
    OUTDOOR = 'O'
    LOCATION_CHOICES = (
            (INDOOR, 'Indoors'),
            (OUTDOOR, 'Outdoors')
        )
    location = models.CharField(max_length=1, choices=LOCATION_CHOICES)
    LOW = 'LO'
    MEDIUM = 'MD'
    HIGH = 'HI'
    ACTIVITY_CHOICES = (
            (LOW, 'Not active'),
            (MEDIUM, 'Somewhat active'),
            (HIGH, 'Very active')
        )
    activity = models.CharField(max_length=2, choices=ACTIVITY_CHOICES)
    
    def __str__(self):
        return self.name
        
    def get_formatted_date(self):
        if self.start_day:
            return self.start_day.strftime("%m/%d/%y")
            
    def get_formatted_time(self):
        if self.start_time:
            return self.start_time.strftime("%H:%M")
    
class EventAttendance(models.Model):
    """ This is a model for dogs attending events. """
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    dog_id = models.ForeignKey('Dog', on_delete=models.CASCADE)