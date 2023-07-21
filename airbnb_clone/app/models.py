from django.db import models
from django.contrib.auth.models import User
import uuid

class Country(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')

    def __str__(self):
        return self.name

class Village(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Name')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

class Views(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

class Place(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    display_image = models.FileField(upload_to='images/', verbose_name='Display Image')
    location = models.CharField(max_length=100, verbose_name='Location')
    village = models.ForeignKey(Village, on_delete=models.CASCADE, verbose_name='Village')
    price = models.IntegerField(verbose_name='Price')
    rating = models.FloatField(verbose_name='Rating')
    guest_capacity = models.IntegerField(verbose_name='Guest Capacity')
    bedrooms = models.IntegerField(verbose_name='Bedrooms')
    beds = models.IntegerField(verbose_name='Beds')
    bathrooms = models.IntegerField(verbose_name='Bathrooms')
    views = models.ManyToManyField(Views, related_name='views', verbose_name='Views')
    has_wifi = models.BooleanField(verbose_name='Has Wifi')
    has_tv = models.BooleanField(verbose_name='Has TV')
    is_available = models.BooleanField(verbose_name='Is Available')
    is_self_check_in = models.BooleanField(verbose_name='Is Self Check In')
    is_pet_friendly = models.BooleanField(verbose_name='Is Pet Friendly')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At', editable=False)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Place')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At', editable=False)
    start_datetime = models.DateTimeField(verbose_name='Start Datetime')
    end_datetime = models.DateTimeField(verbose_name='End Datetime')

    def __str__(self):
        return str(self.id)