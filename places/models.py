from django.db import models
import uuid

from csc.models import City
from users.models import StayWiseUser

class Views(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Name')

    class Meta:
        verbose_name_plural = "Views"

    def __str__(self):
        return self.name

class Place(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, verbose_name='ID', default=uuid.uuid4)
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    owner = models.ForeignKey(StayWiseUser, on_delete=models.CASCADE, verbose_name='Owner')
    display_image = models.FileField(upload_to='images/', verbose_name='Display Image')
    address = models.CharField(max_length=250, verbose_name='address')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Village')
    price = models.IntegerField(verbose_name='Price')
    rating = models.FloatField(verbose_name='Rating')
    guest_capacity = models.IntegerField(verbose_name='Guest Capacity')
    bedrooms = models.IntegerField(verbose_name='Bedrooms')
    beds = models.IntegerField(verbose_name='Beds')
    bathrooms = models.IntegerField(verbose_name='Bathrooms')
    views = models.ManyToManyField(Views, related_name='views', verbose_name='Views')
    has_wifi = models.BooleanField(verbose_name='Has Wifi', default=False)
    has_tv = models.BooleanField(verbose_name='Has TV', default=False)
    is_available = models.BooleanField(verbose_name='Is Available', default=False)
    is_self_check_in = models.BooleanField(verbose_name='Is Self Check In', default=False)
    is_pet_friendly = models.BooleanField(verbose_name='Is Pet Friendly', default=False)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Created At', editable=False)
    updatedAt =  models.DateTimeField(auto_now=True, verbose_name='Updated At', editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        db_table = 'staywise_place'
        managed = True