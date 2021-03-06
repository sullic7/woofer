""" This module holds the models for the Woofer app."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from woofer.validators import validate_date, validate_greater_than_or_equal_zero

class Profile(models.Model):
    """ This is a profile model of the django user model. More info here
    https://docs.djangoproject.com/en/1.9/topics/auth/customizing/"""
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    phone_number = models.IntegerField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True,\
        null=True, validators=[validate_date])

    def __str__(self):
        """ This method is used to provide a string represenation for the
        Django admin interface.
        """
        return self.user.username

    def get_formatted_birthday(self):
        """ Return a formated string holding the users birthday. """
        if self.birthday:
            return self.birthday.strftime("%m/%d/%y")

class Dog(models.Model):
    """ This is a model for dogs which are owned by one user. """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True,
                                null=True, validators=[validate_date])
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

    def __str__(self):
        """ This method is used to provide a string represenation for the
        Django admin interface.
        """
        return self.name

    def get_formatted_birthday(self):
        """ Return a formated string holding the dog's birthday."""
        if self.birthday:
            return self.birthday.strftime("%m/%d/%y")

class Event(models.Model):
    """ This is a model for events created by one user."""
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
    attendance_cap = models.IntegerField(default=0,
                                         validators=[validate_greater_than_or_equal_zero])
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
        """ This method is used to provide a string represenation for the
        Django admin interface.
        """
        return self.name

    def get_formatted_date(self):
        """ Return a formated string holding the event's date."""
        if self.start_day:
            return self.start_day.strftime("%m/%d/%y")

    def get_formatted_time(self):
        """ Return a formated string holding the event's time."""
        if self.start_time:
            return self.start_time.strftime("%H:%M")

class EventAttendance(models.Model):
    """ This is a model for dogs attending events. """
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    dog = models.ForeignKey('Dog', on_delete=models.CASCADE)

    def __str__(self):
        """ This method is used to provide a string represenation for the
        Django admin interface.
        """
        return ("%s's Dog %s is attending %s" %
                (self.dog.owner.username, self.dog.name, self.event.name))
