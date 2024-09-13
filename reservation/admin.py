# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import PlaceReservation


@admin.register(PlaceReservation)
class PlaceReservationAdmin(admin.ModelAdmin):
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
        'start_datetime',
        'end_datetime',
        'registered_at',
    )
