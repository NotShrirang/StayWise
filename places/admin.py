# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Views, Place


@admin.register(Views)
class ViewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'owner',
        'display_image',
        'address',
        'city',
        'price',
        'rating',
        'guest_capacity',
        'bedrooms',
        'beds',
        'bathrooms',
        'has_wifi',
        'has_tv',
        'is_available',
        'is_self_check_in',
        'is_pet_friendly',
        'createdAt',
        'updatedAt',
    )
    list_filter = (
        'owner',
        'city',
        'has_wifi',
        'has_tv',
        'is_available',
        'is_self_check_in',
        'is_pet_friendly',
        'createdAt',
        'updatedAt',
    )
    raw_id_fields = ('views',)
    search_fields = ('name',)
