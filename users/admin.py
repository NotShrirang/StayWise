# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import StayWiseUser


@admin.register(StayWiseUser)
class StayWiseUserAdmin(admin.ModelAdmin):
    list_display = (
        'password',
        'last_login',
        'id',
        'email',
        'firstName',
        'lastName',
        'gender',
        'dateOfBirth',
        'bio',
        'profilePicture',
        'city',
        'phoneNumber',
        'createdAt',
        'updatedAt',
        'isVerified',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'last_login',
        'dateOfBirth',
        'city',
        'createdAt',
        'updatedAt',
        'isVerified',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
    )
    raw_id_fields = ('groups', 'user_permissions')
