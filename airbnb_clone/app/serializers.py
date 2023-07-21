from rest_framework import serializers
from .models import Place, Country, State, Village, Views, Reservation

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'country')

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ('id', 'name', 'state')

class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = ('id', 'name')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'display_image', 'location', 'village', 'price', 'rating', 'guest_capacity', 'bedrooms', 'beds', 'bathrooms', 'views', 'has_wifi', 'has_tv', 'is_available', 'is_self_check_in', 'is_pet_friendly', 'created_at')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'place', 'user', 'created_at', 'start_datetime', 'end_datetime')
