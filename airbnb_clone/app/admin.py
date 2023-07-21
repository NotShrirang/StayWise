from django.contrib import admin
from .models import Country, State, Village, Views, Place, Reservation

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Village)
admin.site.register(Views)
admin.site.register(Place)
admin.site.register(Reservation)