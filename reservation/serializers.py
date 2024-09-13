from rest_framework import serializers
from .models import PlaceReservation

class PlaceReservationSerializer(serializers.ModelSerializer):
    placeName = serializers.CharField(source='place.name')
    placeAddress = serializers.CharField(source='place.address')
    userName = serializers.CharField(source='user.firstName')
    userEmail = serializers.CharField(source='user.email')

    class Meta:
        model = PlaceReservation
        fields = ['id', 'place', 'placeName', 'placeAddress', 'user', 'userName', 'userEmail', 'userPhoneNumber', 'start_datetime', 'end_datetime', 'registered_at']