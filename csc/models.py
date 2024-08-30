from django.db import models
from django.contrib.auth.models import User
import uuid

class Country(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class State(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "States"
    

class City(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name='Name')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"