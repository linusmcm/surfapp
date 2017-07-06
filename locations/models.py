from __future__ import unicode_literals
from django.db import models
#from profiles.models import profile


# Create your models here.
class Country(models.Model):

    # Fields
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('locations.Country', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "State"



class Region(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('locations.State', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Region"



class Location(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()
    best_wind_direct = models.CharField(max_length=30)
    break_type = models.TextField(max_length=100)
    local_attitude = models.TextField(max_length=100)
    best_wind = models.TextField(max_length=100)
    best_tide = models.TextField(max_length=100)
    wave_type = models.TextField(max_length=100)
    who_are_locals = models.ManyToManyField('profiles.profile',)
    who_are_locals_ID = models.TextField(max_length=100)
    region = models.TextField(max_length=100)
    # Relationship Fields
    country = models.ForeignKey('locations.Region', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Location"