from django.db import models
from django.contrib.auth.models import User
import uuid

class Country(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        db_table = "country"
        managed = True


class State(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        db_table = "state"
        managed = True
    

class City(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        db_table = "city"
        managed = True