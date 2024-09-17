# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Reservation, Ratings


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'place',
        'user',
        'start_datetime',
        'end_datetime',
        'registered_at',
    )
    list_filter = (
        'place',
        'user',
        'start_datetime',
        'end_datetime',
        'registered_at',
    )


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'user', 'remarks')
    list_filter = ('reservation', 'user')
